# src/api_client.py
import pandas as pd
import requests
from io import StringIO

BASE_URL = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-national-tr/records"

def fetch_eco2mix_data(rows = 500):
    batch_size = 100  # OpenData limits to 100 rows per call
    all_records = []

    for offset in range(0, rows, batch_size):
        params = {
            "limit": batch_size,
            "offset": offset,
            "timezone": "Europe/Paris",
            "order_by": "date DESC"
        }

        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            records = data.get("results", [])
            all_records.extend(records)

            # Stop early if less data than batch_size = no more data
            if len(records) < batch_size:
                break

        except Exception as e:
            print(f"Erreur lors du chargement des données (offset {offset}) : {e}")
            break

    # Into datagrame
    if all_records:
        df = pd.json_normalize(all_records)
        return df
    else:
        return pd.DataFrame()