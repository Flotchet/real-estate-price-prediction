from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

import sys
#add the path to data_aquisition.py to the current working space
sys.path.append('/home/flotchet/Becode/LIE-Thomas-2-main/content/0.projects/2.immo_eliza/a_data_acquisition')

from data_aquisition import *

# Path: f_apache_airflow/automation.py

default_args = {
    'owner': 'Flotchet',
    'depends_on_past': False,
    'start_date': datetime(year = 2023, month = 3, day = 6)
    }

dag = DAG('f_apache_airflow', default_args = default_args, schedule_interval = "0 12 32 * *")

t1 = PythonOperator(
    task_id='Scrape',
    python_callable=immoweb_scraper(),
    dag=dag
)

t1