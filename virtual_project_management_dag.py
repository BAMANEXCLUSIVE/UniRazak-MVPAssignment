from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define subtasks
def project_selection(**kwargs):
    print("Subtask: Project selection process completed. Objective: Create an e-commerce platform for students.")

def team_formation(**kwargs):
    print("Subtask: Team formation completed. Roles assigned: Project Manager, Backend Developer, Frontend Developer, Business Analyst, Quality Analyst.")

def planning_phase(**kwargs):
    print("Subtask: Project planning completed. Milestones, deliverables, and timelines defined.")

def collaboration_setup(**kwargs):
    print("Subtask: Collaboration tools setup completed. Using Trello for task management, Microsoft Teams for communication.")

def execution_phase(**kwargs):
    print("Subtask: Project execution ongoing. Tasks assigned, and progress tracked.")

def mid_project_reporting(**kwargs):
    print("Subtask: Mid-project report generated. Summary of progress, challenges, and adjustments.")

def final_reporting(**kwargs):
    print("Subtask: Final report generated. Documenting accomplishments, lessons learned, and insights.")

def presentation_prep(**kwargs):
    print("Subtask: Presentation prepared. Highlighting key achievements and project outcomes.")

def update_beunixcsuite_workflow():
    import subprocess
    subprocess.run(["python", "/workspaces/BEunixCsuite/beunixcsuite_workflow.py"], check=True)

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'virtual_project_management_workflow',
    default_args=default_args,
    description='Automated workflows for virtual project management assignment',
    schedule_interval=None,
    start_date=datetime(2025, 4, 10),
    catchup=False,
) as dag:

    # Subtasks as PythonOperators
    task_project_selection = PythonOperator(
        task_id='project_selection',
        python_callable=project_selection,
        provide_context=True,
    )

    task_team_formation = PythonOperator(
        task_id='team_formation',
        python_callable=team_formation,
        provide_context=True,
    )

    task_planning_phase = PythonOperator(
        task_id='planning_phase',
        python_callable=planning_phase,
        provide_context=True,
    )

    task_collaboration_setup = PythonOperator(
        task_id='collaboration_setup',
        python_callable=collaboration_setup,
        provide_context=True,
    )

    task_execution_phase = PythonOperator(
        task_id='execution_phase',
        python_callable=execution_phase,
        provide_context=True,
    )

    task_mid_project_reporting = PythonOperator(
        task_id='mid_project_reporting',
        python_callable=mid_project_reporting,
        provide_context=True,
    )

    task_final_reporting = PythonOperator(
        task_id='final_reporting',
        python_callable=final_reporting,
        provide_context=True,
    )

    task_presentation_prep = PythonOperator(
        task_id='presentation_prep',
        python_callable=presentation_prep,
        provide_context=True,
    )

    update_workflow_task = PythonOperator(
        task_id='update_beunixcsuite_workflow',
        python_callable=update_beunixcsuite_workflow,
    )

    # Establish task dependencies
    task_project_selection >> task_team_formation >> task_planning_phase >> task_collaboration_setup >> task_execution_phase
    task_execution_phase >> task_mid_project_reporting >> task_final_reporting >> task_presentation_prep >> update_workflow_task
