from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

import sys
#add the path to data_aquisition.py to the current working space

from data_aquisition import *

# Path: f_apache_airflow/automation.py

default_args = {
    'owner': 'Admin',
    'depends_on_past': False,
    'start_date': datetime(year = 2023, month = 3, day = 6)
    }

dag = DAG('f_apache_airflow', default_args = default_args, schedule_interval = "0 20 30 * *")

t1 = PythonOperator(
    task_id='Scrape',
    python_callable=immoweb_scraper(),
    dag=dag
)

t1