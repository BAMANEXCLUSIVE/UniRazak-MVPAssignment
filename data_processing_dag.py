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

def update_beunixcsuite_workflow():
    import subprocess
    subprocess.run(["python", "/workspaces/BEunixCsuite/beunixcsuite_workflow.py"], check=True)

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

    update_workflow_task = PythonOperator(
        task_id='update_beunixcsuite_workflow',
        python_callable=update_beunixcsuite_workflow,
    )

    data_processing_task >> update_workflow_task
