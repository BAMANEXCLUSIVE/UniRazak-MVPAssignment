# Use the official Apache Airflow image
FROM apache/airflow:2.10.5

# Set the working directory
WORKDIR /opt/airflow

# Copy your DAGs into the Airflow DAGs directory
COPY --chown=airflow:root test_dag.py /opt/airflow/dags/