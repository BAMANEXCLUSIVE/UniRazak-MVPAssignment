from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a Python function for the task
def update_project_data():
  print("Project data updated successfully!")

# Define the DAG
default_args = {
  'owner': 'airflow',
  'depends_on_past': False,
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
}

with DAG(
  dag_id='project_management_updates',
  default_args=default_args,
  description='Automates project management updates',
  schedule_interval='@daily',
  start_date=datetime(2023, 1, 1),
  catchup=False,
  tags=['project', 'management'],
) as dag:

  # Define a task
  update_task = PythonOperator(
    task_id='update_project_data',
    python_callable=update_project_data,
  )

  # Set task dependencies (if needed)
  update_task