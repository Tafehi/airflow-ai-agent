from airflow.decorators import dag, task
from airflow.sensors.base import PokeReturnValue
from airflow.hooks.base import BaseHook
from datetime import datetime
import requests

@dag(
    start_date=datetime(2023, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['stock_market'],
)
def stock_market():
    @task.sensor(poke_interval=30, timeout=300, mode='poke')
    def is_api_available() -> PokeReturnValue:
        api = BaseHook.get_connection("stock_api")
        url = f"{api.host}{api.extra_dejson.get('endpoint')}"
        print(f"Checking API availability at {url}")
        try:
            response = requests.get(url, headers=api.extra_dejson.get('headers'))
            if response.status_code == 200:
                print("API is available")
                return PokeReturnValue(True)
            else:
                print(f"API returned status code {response.status_code}")
                return PokeReturnValue(False)
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return PokeReturnValue(False)

    is_api_available()

stock_market()
