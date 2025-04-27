<link rel="stylesheet" type="text/css" href="../style.css">
# Project Management Tool

## Brief Description
The Project Management Tool is designed to help teams manage projects efficiently by providing core functionalities such as task management, resource allocation, and chaos engineering integration. It also includes a user-friendly interface for easy navigation and reporting.

## Instructions for Setting Up and Running the Project

### Prerequisites
- Node.js (v14.x or later)
- npm (v6.x or later)
- Python (v3.8 or later)
- Apache Airflow (v2.0 or later)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/BAMANEXCLUSIVE/UniRazak-MVPAssignment.git
   cd UniRazak-MVPAssignment
   ```

2. Install Node.js dependencies:
   ```sh
   npm install
   ```

3. Set up the Python virtual environment and install dependencies:
   ```sh
   python3 -m venv airflow_env
   source airflow_env/bin/activate
   pip install -r requirements.txt
   ```

4. Initialize the Airflow database:
   ```sh
   airflow db init
   ```

5. Start the Airflow web server and scheduler:
   ```sh
   airflow webserver --port 8080
   airflow scheduler
   ```

### Running the Project

1. Start the Node.js server:
   ```sh
   npm start
   ```

2. Access the Project Management Tool in your web browser:
   ```
   http://localhost:3000
   ```

3. Access the Airflow web interface:
   ```
   http://localhost:8080
   ```

### Sample DAG for Project Management Updates

Below is a sample Directed Acyclic Graph (DAG) for automating project management updates using Apache Airflow:

```python
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
```

For more information on Apache Airflow, refer to the [official documentation](https://airflow.apache.org/docs/).
