from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 
from datetime import datetime, timedelta
import os

default_dag_args = { 'start_date': datetime(2022, 1, 1),
 'email_on_failure': False, 'email_on_retry': False,
  'retries': 1, 'retry_delay': timedelta(minutes=5), 'project_id': 1 }

with DAG("First_DAG", schedule_interval = None, default_args = default_dag_args) as dag:    
  task_0 = BashOperator(task_id = 'bash_task', bash_command = "echo 'command executed from Bash Operator' ")
  task_1 = BashOperator(task_id = 'bash_task_move_data', bash_command = "cp /Users/Username/develhope_file/DATA_CENTER/DATA_LAKE/dataset_raw.txt  /Users/Username/develhope_file/DATA_CENTER/CLEAN_DATA")
  task_2 = BashOperator(task_id = 'bash_task_move_data', bash_command = "os.remove(/Users/Username/develhope_file/DATA_CENTER/DATA_LAKE/dataset_raw.txt)")

task_0 >> task_1 >> task_2
