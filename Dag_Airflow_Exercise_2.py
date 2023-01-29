from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

def python_dt():
    print(datetime.now())

default_dag_args = {
    'start_date': datetime(2022, 9, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1
}

with DAG("dtnow_python_op", schedule_interval = None, default_args) as dag_python:
    task_0 = PythonOperator(task_id= 'dtnow_python_op', python_callable = python_dt)

