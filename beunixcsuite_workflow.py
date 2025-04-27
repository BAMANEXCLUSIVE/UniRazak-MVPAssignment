import os
import subprocess
import sys
import time
import logging

print("Modules are available.")

# Configure logging
log_file = 'beunixcsuite_workflow.log'
if not os.path.exists(log_file):
    open(log_file, 'w').close()

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Task statuses
task_status = {}

# Ensure all script files exist
def ensure_file_exists(file_path):
    """Creates an empty file if it doesn't exist."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

# Define tasks and their dependencies
tasks = {
    "InstallationAndSetup": {
        "script": "/workspaces/BEunixCsuite/installation_and_setup.py",
        "dependencies": []
    },
    "EnvironmentSetup": {
        "script": "/workspaces/BEunixCsuite/environment_setup.py",
        "dependencies": ["InstallationAndSetup"]
    },
    "DataProcessing": {
        "script": "/workspaces/BEunixCsuite/data_processing.py",
        "dependencies": ["EnvironmentSetup"]
    },
    "AutomationAndWorkflows": {
        "script": "/workspaces/BEunixCsuite/automation_workflows.py",
        "dependencies": ["DataProcessing"]
    },
    "Documentation": {
        "script": "/workspaces/BEunixCsuite/documentation.py",
        "dependencies": []
    },
    "VersioningAndUpgrades": {
        "script": "/workspaces/BEunixCsuite/versioning_upgrades.py",
        "dependencies": ["InstallationAndSetup"]
    },
    "MLAndAI": {
        "script": "/workspaces/BEunixCsuite/ml_and_ai.py",
        "dependencies": ["DataProcessing"]
    },
    "DatabaseAndBackend": {
        "script": "/workspaces/BEunixCsuite/database_backend.py",
        "dependencies": ["InstallationAndSetup"]
    },
    "StatisticsAndAnalysis": {
        "script": "/workspaces/BEunixCsuite/statistics_analysis.py",
        "dependencies": ["DataProcessing", "MLAndAI"]
    },
    "DataProcessingDAG": {
        "script": "/workspaces/BEunixCsuite/data_processing_dag.py",
        "dependencies": ["DataProcessing"]
    },
    "VirtualProjectManagementDAG": {
        "script": "/workspaces/BEunixCsuite/virtual_project_management_dag.py",
        "dependencies": ["DataProcessing"]
    },
    "MarketingProjectManagement": {
        "script": "/workspaces/BEunixCsuite/marketing_project_management.py",
        "dependencies": ["DataProcessing"]
    },
    "BuildAndDeploymentFailureHandler": {
        "script": "/workspaces/BEunixCsuite/build_deployment_failure_handler.py",
        "dependencies": []
    }
}

# Ensure all task scripts exist
for task in tasks.values():
    ensure_file_exists(task["script"])

# Function to execute a task
def execute_task(task_name):
    """Executes a script and tracks its progress"""
    task = tasks[task_name]
    script_path = task["script"]

    # Check dependencies
    for dependency in task["dependencies"]:
        if task_status.get(dependency) != "success":
            logging.warning(f"Task {task_name} is waiting for dependency {dependency} to complete.")
            return "waiting"

    try:
        # Run the script
        logging.info(f"Starting task: {task_name}")
        subprocess.run(["python", script_path], check=True)
        logging.info(f"Task {task_name} completed successfully.")
        task_status[task_name] = "success"
        return "success"
    except subprocess.CalledProcessError as e:
        logging.error(f"Task {task_name} failed: {e}")
        task_status[task_name] = "failed"
        return "failed"

# Monitor and run tasks
def run_workflow():
    """Executes the full workflow"""
    all_tasks = list(tasks.keys())
    while all_tasks:
        for task_name in all_tasks[:]:  # Iterate over a copy of the list
            status = execute_task(task_name)
            if status in ["success", "failed"]:
                all_tasks.remove(task_name)  # Remove completed or failed tasks

        # Pause to avoid overloading
        time.sleep(5)

    logging.info("Workflow completed!")

def check_python_environment():
    """Check and fix Python environment variables."""
    python_home = os.environ.get("PYTHONHOME")
    python_path = os.environ.get("PYTHONPATH")

    if python_home or python_path:
        print("Environment variables PYTHONHOME or PYTHONPATH are set. Clearing them...")
        os.environ.pop("PYTHONHOME", None)
        os.environ.pop("PYTHONPATH", None)
        print("Cleared PYTHONHOME and PYTHONPATH.")

    print("Verifying Python installation...")
    try:
        subprocess.run([sys.executable, "--version"], check=True)
        print("Python installation is valid.")
    except subprocess.CalledProcessError:
        print("Python installation is invalid. Reinstalling Python...")
        reinstall_python()

def reinstall_python():
    """Reinstall Python automatically."""
    python_installer_url = "https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe"
    installer_path = "python_installer.exe"

    print(f"Downloading Python installer from {python_installer_url}...")
    subprocess.run(["curl", "-o", installer_path, python_installer_url], check=True)

    print("Running Python installer...")
    subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)

    print("Python reinstallation completed. Cleaning up installer...")
    os.remove(installer_path)

    # Restart the script after reinstalling Python
    print("Restarting the script...")
    os.execv(sys.executable, [sys.executable] + sys.argv)

# Main script entry point
if __name__ == "__main__":
    check_python_environment()
    logging.info("Starting the BEunixCsuite workflow...")
    run_workflow()
