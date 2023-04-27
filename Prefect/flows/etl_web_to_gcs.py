from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from random import randint
import os
import numpy as np

@task(retries=3)
def extract_dataset(dataset_url: str) -> pd.DataFrame:
    """Download US Accidentes dataset"""
    print(f"Reading file {dataset_url}")
    os.environ['KAGGLE_USERNAME'] = "tomasuzquiano"
    os.environ['KAGGLE_KEY'] = "2de3d8f0f28aa67bd713cd78ba25f683"
    download_dataset = os.system("mkdir dataset_folder;cd dataset_folder;kaggle datasets download -d 'sobhanmoosavi/us-accidents'")
    df = pd.read_csv('dataset_folder/us-accidents.zip', compression='zip')

    return df


@task(log_prints=True)
def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Select columns"""
    df = df[["ID", "Severity", "Start_Time", "End_Time", "Description", "State", "Weather_Condition"]]

    """Look for unknown and NAN"""
    str_features = ['Description', 'State', 'Weather_Condition']
    df[str_features] = df[str_features].fillna('Unknown')
    df[str_features] = df[str_features].replace(np.nan, 'Unknown')
    df["ID"] = df["ID"].fillna(2)
    df["ID"] = df["ID"].replace(np.nan, 2)
    
    """Fix dtype issues"""
    df.ID = df.ID.astype('str')
    df.Severity = df.Severity.astype('int')
    #df['Start_Date'] = pd.to_datetime(df['Start_Time']).dt.strftime('%Y-%m-%d')
    #df['End_Date'] = pd.to_datetime(df['End_Time']).dt.strftime('%Y-%m-%d')
    df['Start_Time'] = df['Start_Time'].str.slice(0, 10)
    df['End_Time'] = df['End_Time'].str.slice(0, 10)
    df.Description = df.Description.astype('str')
    df.State = df.State.astype('str')
    df.Weather_Condition = df.Weather_Condition.astype('str')
    
    #df = df.drop(['Start_Time','End_Time'], axis=1)
    """Print some important data"""
    print(df.head(2))
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")

    return df


@task()
def write_local(df: pd.DataFrame) -> Path:
    """Write DataFrame out locally as parquet file"""
    path = Path(f"dataset_folder/us-accidents.parquet")
    df.to_parquet(path, compression="gzip")

    return path


@task()
def write_gcs(path: Path) -> None:
    """Upload local parquet file to GCS"""
    gcs_block = GcsBucket.load("project-gcs")
    gcs_block.upload_from_path(from_path=path, to_path=path)

    return


@flow()
def etl_web_to_gcs() -> None:
    """The main ETL function"""
    dataset_url = f"https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/download?datasetVersionNumber=12"
    dataset_raw = extract_dataset(dataset_url)
    dataset_clean = clean_dataset(dataset_raw)
    path = write_local(dataset_clean)
    write_gcs(path)


if __name__ == "__main__":
    etl_web_to_gcs()
