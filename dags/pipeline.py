from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
LOCAL_PATH = "/opt/airflow/data/winequality.csv"

def download_data():
    response = requests.get(URL)
    with open(LOCAL_PATH, 'wb') as f:
        f.write(response.content)

def validate_data():
    try:
        df = pd.read_csv(LOCAL_PATH)
        print(f"{len(df)} rows loaded.")
    except Exception as e:
        raise ValueError("Invalid or missing data") from e

def transform_data_1():
    df = pd.read_csv(LOCAL_PATH)
    df['Index'] = df.index
    df.to_csv("/opt/airflow/data/transformed_1.csv", index=False)
    print("Tache transform_data bien executee")

def transform_data_2():
    df = pd.read_csv(LOCAL_PATH)
    df_filtered = df[df.columns[:2]]
    df_filtered.to_csv("/opt/airflow/data/transformed_2.csv", index=False)

def final_task():
    print("Final task depends on both transformations.")

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG("data_pipeline_demo",
         schedule_interval=None,
         default_args=default_args,
         catchup=False) as dag:

    t1 = PythonOperator(task_id='download_data', python_callable=download_data)
    t2 = PythonOperator(task_id='validate_data', python_callable=validate_data)
    t3 = PythonOperator(task_id='transform_data_1', python_callable=transform_data_1)
    t4 = PythonOperator(task_id='transform_data_2', python_callable=transform_data_2)
    t5 = PythonOperator(task_id='final_task', python_callable=final_task)

    t1 >> t2 >> [t3, t4] >> t5
