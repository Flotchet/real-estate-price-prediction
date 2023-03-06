from airflow.models import DAG
from airflow.hooks.bash_operator import BashOperator
from datetime import datetime

import sys
#add the path to data_aquisition.py to the current working space
sys.path.append('a_data_acquisition')
#add the path to data_preparation_for_regression.py to the current working space
sys.path.append('b_data_preparation')
#add the path to model.py to the current working space
sys.path.append('d_Machine_learning/model_training')

# Path: f_apache_airflow/automation.py

default_args = {
    'owner': 'Flotchet',
    'depends_on_past': False,
    'start_date': datetime(year = 2023, month = 3, day = 6)
    }

dag = DAG('f_apache_airflow', default_args = default_args, schedule_interval = "0 12 32 * *")

t1 = BashOperator(
    task_id = 'Scrape',
    bash_command = 'python3 automation.py',
    dag = dag)

t2 = BashOperator(
    task_id = 'prepare',
    bash_command = 'python3 data_preparation_for_regression.py',
    dag = dag)

t3 = BashOperator(
    task_id = 'model',
    bash_command = 'python3 model.py',
    dag = dag)

t1 >> t2 >> t3