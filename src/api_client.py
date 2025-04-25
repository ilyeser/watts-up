import requests
import pandas as pd

def fetch_eco2mix_data(rows=500) -> pd.DataFrame:
    url = "https://odre.opendatasoft.com/api/records/1.0/search/"
    params = {
        "dataset": "eco2mix-national-tr",
        "rows": rows,
        "sort": "date_heure"
    }

    try:
        r = requests.get(url, params=params)
        r.raise_for_status()
        records = r.json()["records"]
        data = [rec["fields"] for rec in records]
        return pd.DataFrame(data)
    except Exception as e:
        print("Erreur API:", e)
        return pd.DataFrame()
