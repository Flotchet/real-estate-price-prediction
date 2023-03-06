from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

import os
#add the path to data_aquisition.py to the current working space
os.chdir('a_data_acquisition')

# Path: f_apache_airflow/automation.py

default_args = {
    'owner': 'Flotchet',
    'depends_on_past': False,
    'start_date': datetime(year = 2023, month = 3, day = 6)
    }

dag = DAG('f_apache_airflow', default_args = default_args, schedule_interval = "0 20 * * *")

t1 = BashOperator(
    task_id = 'print_date',
    bash_command = 'date',
    dag = dag)

t2 = BashOperator(
    task_id = 'sleep',
    bash_command = 'sleep 5',
    retries = 3,
    dag = dag)

t1 >> t2

