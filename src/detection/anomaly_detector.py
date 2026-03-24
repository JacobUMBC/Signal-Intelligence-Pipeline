import pandas as pd
import os
from src.processing.fft_processor import PROCESSED_CSV

ANOMALY_CSV = os.path.join(os.path.dirname(PROCESSED_CSV), "anomalies.csv")

def run_anomaly_detector():
    df = pd.read_csv(PROCESSED_CSV)

    # Simple anomaly detection
    if 'processed_signal' in df.columns:
        mean = df['processed_signal'].mean()
        std = df['processed_signal'].std()
        df['anomaly'] = df['processed_signal'] > (mean + 2 * std)

    df.to_csv(ANOMALY_CSV, index=False)
    print(f"✅ Anomalies saved to {ANOMALY_CSV}")