#from airflow import DAG
from airflow.decorators import dag, task
from datetime import datetime





@dag(
    start_date=datetime(2023, 1, 1),
    schedule='@daily',  
    catchup=False,
    tags=['taskflow'],
)

def taskflow():

  @task
  def task_one():
      print("Task One executed")
      return 42

  @task
  def task_two(value):
      print("Task Two executed")
      print(value)  # Pull the result from task_one
      return "Task Two completed"
  
  tasks = task_two(task_one())

taskflow_dag = taskflow()