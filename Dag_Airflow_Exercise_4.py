pip3 install apache-airflow-providers-postgres
import time
import json 
from airflow import DAG 
from airflow.operators.postgres_operator 
import PostgresOperator 
from datetime import timedelta
from airflow.utils.dates import days_ago

default_args = { 'owner': 'airflow',
'retries': 1, 'retry_delay': timedelta(minutes=5), }

create_query = """
DROP TABLE IF EXISTS public.empployees_table 
CREATE TABLE public.emp_table(id INT NOT NULL, name VARCHAR(100) NOT NULL, age ID;"""

insert_data_query = """
INSERT INTO public.employees_table(id, name, age)
VALUES (1, 'John', 35),(2, 'Mary',29),(3,'Jim',42);
"""

calculating_averag_age = """SELECT AVG(AGE) FROM public.employees_table; 
"""

dag_postgres = 
    DAG(dag_id = "postgres_dag_connection",
    default_args = default_args, 
    schedule_interval = None, 
    start_date = days_ago(1))
    
create_table = 
PostgresOperator(task_id = "creation_of_table",
                 sql = create_query, dag = dag_postgres,
                 postgres_conn_id = "postgres_user_local")

insert_data = 
PostgresOperator(task_id = "insertion_of_data",
                 sql = insert_data_query,
                 dag = dag_postgres, 
                 postgres_conn_id = "postgres_user_local")

group_data = 
PostgresOperator(task_id = "calculating_averag_age",
                 sql = calculating_averag_age, 
                 dag = dag_postgres, 
                 postgres_conn_id = "postgres_user_local")

create_table >> insert_data >> group_data
