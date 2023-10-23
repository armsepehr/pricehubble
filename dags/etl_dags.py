from core.extract import Extractor
from core.transform import Transformer
from core.load import Loader

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

e = Extractor()
t = Transformer(e.load())
l = Loader()

dag = DAG(
    dag_id='etl_dag',
    start_date=datetime(2023, 10, 1),
    schedule='@daily',
    tags=["take-home-assignment"],
)

# extraction 
e_task = PythonOperator(task_id='e_task',python_callable=e.load,dag=dag)

# transformation
t_invalidate_task = PythonOperator(task_id='t_invalidate',python_callable=t.drop_invalidate_data,dag=dag)
t_price_task = PythonOperator(task_id='t_price',python_callable=t.get_price,dag=dag)
t_format_task = PythonOperator(task_id='t_format',python_callable=t.convert_format,dag=dag)
t_requirement_task = PythonOperator(task_id='t_requirement',python_callable=t.requirement,dag=dag)

# load
l_store = PythonOperator(task_id='l_store',python_callable=l.store,dag=dag)
e_task >> [t_invalidate_task,t_price_task,t_format_task,t_requirement_task] >> l_store