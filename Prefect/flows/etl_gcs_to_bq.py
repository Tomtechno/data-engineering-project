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
    schema = [
        bigquery.SchemaField('ID', field_type="STRING")
        bigquerySchemaField('Severity', field_type="INTEGER")
        bigquerySchemaField('Start_Date', field_type="TIMESTAMP")
        bigquerySchemaField('End_Date', field_type="TIMESTAMP")
        bigquerySchemaField('Description', field_type="STRING")
        bigquerySchemaField('State', field_type="STRING")
        bigquerySchemaField('Weather_Condition', field_type="STRING")
    ]
    df.to_gbq(
        destination_table="",
        project_id="",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
        table_schema=schema
    )
    print(f"Data loaded to big query, table: {}")

@flow()
def etl_gcs_to_bq():
    """Main ETL flow to load data into Big Query"""
    path = extract_from_gcs()
    df = pd.read_parquet(path)
    write_bq(df)


if __name__ == "__main__":
    etl_gcs_to_bq()
