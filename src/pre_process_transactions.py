import pandas as pd
import json

transactions = pd.read_json("../data/raw/transactions.json", encoding = "UTF-8")

transactions["offer_id"] = transactions["value"].apply(lambda x: x.get("offer id") if isinstance(x, dict) else None)
transactions["reward"] = transactions["value"].apply(lambda x: x.get("reward") if isinstance(x, dict) else None)
transactions["amount"] = transactions["value"].apply(lambda x: x.get("amount") if isinstance(x, dict) else None)

transactions_clean = transactions.drop(columns=["value"])

transactions_clean.to_json("../data/processed/transactions_clean.json")
