# src/db/db_connector.py
import pandas as pd
from sqlalchemy import create_engine
import os

POSTGRES_HOST = "127.0.0.1"
POSTGRES_PORT = "5432"
POSTGRES_USER = "admin"
POSTGRES_PASSWORD = "secret"
POSTGRES_DB = "signals"

engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

def push_to_db():
    # Push processed signals
    if os.path.exists("processed_signal.csv"):
        df = pd.read_csv("processed_signal.csv")
        df.to_sql("processed_signals", engine, if_exists="replace", index=False)
        print("✅ CSV successfully saved to PostgreSQL table 'processed_signals'!")

    # Push anomalies as a separate table
    if os.path.exists("anomalies.csv"):
        df_anom = pd.read_csv("anomalies.csv")
        df_anom.to_sql("anomalies", engine, if_exists="replace", index=False)
        print("✅ Anomalies CSV saved to PostgreSQL table 'anomalies'!")