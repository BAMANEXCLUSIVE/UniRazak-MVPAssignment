from airflow import DAG # type: ignore
from airflow.operators.python import PythonOperator # type: ignore
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_data_processing():
    import subprocess
    subprocess.run(["python", "/workspaces/BEunixCsuite/data_processing.py"], check=True)

with DAG(
    'data_processing_workflow',
    default_args=default_args,
    description='Data Processing Workflow for BEunixCsuite',
    schedule_interval=None,
    start_date=datetime(2025, 4, 9),
    catchup=False,
) as dag:

    data_processing_task = PythonOperator(
        task_id='run_data_processing',
        python_callable=run_data_processing,
    )

    data_processing_task
