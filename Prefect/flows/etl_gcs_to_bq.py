from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
from google.cloud import bigquery


@task(retries=3)
def extract_from_gcs() -> Path:
    """Download us accidents data from GCS"""
    gcs_path = f"dataset_folder/us-accidents.parquet"
    gcs_block = GcsBucket.load("project-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"../dataset_folder/")

    return Path(f"../dataset_folder/{gcs_path}")


@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""
    gcp_credentials_block = GcpCredentials.load("project-gcp-creds") 
    #schema = [bigquery.SchemaField('ID', field_type="STRING"), bigquery.SchemaField('Severity', field_type="INTEGER"), bigquery.SchemaField('Description', field_type="STRING"), bigquery.SchemaField('State', field_type="STRING"), bigquery.SchemaField('Weather_Condition', field_type="STRING"), bigquery.SchemaField('Start_Date', field_type="TIMESTAMP"), bigquery.SchemaField('End_Date', field_type="TIMESTAMP")]
    df.to_gbq(
        destination_table="de_project_dataset.us_accidents",
        project_id="data-engineer-project-384504",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
        table_schema=None
    )



@flow()
def etl_gcs_to_bq():
    """Main ETL flow to load data into Big Query"""
    path = extract_from_gcs()
    df = pd.read_parquet(path)
    write_bq(df)


if __name__ == "__main__":
    etl_gcs_to_bq()
