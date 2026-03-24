import numpy as np
import pandas as pd
import os
from src.signal_generator.generator import OUTPUT_CSV

# Absolute paths
RAW_CSV = OUTPUT_CSV
PROCESSED_CSV = os.path.join(os.path.dirname(RAW_CSV), "processed_signal.csv")

def run_fft_processor():
    # Read raw signal
    df = pd.read_csv(RAW_CSV)
    print(f"✅ Loaded {RAW_CSV}, first 5 rows:\n{df.head()}")

    # FFT processing
    y = df['amplitude'].values
    n = len(y)
    # Sampling interval from time column
    dt = df['time'][1] - df['time'][0]
    freq = np.fft.rfftfreq(n, d=dt)
    magnitude = np.abs(np.fft.rfft(y))

    # Prepare processed DataFrame
    df_fft = pd.DataFrame({
        "frequency": freq,
        "magnitude": magnitude,
        "processed_signal": magnitude  # keep this for anomaly detection
    })

    # Save processed signal
    df_fft.to_csv(PROCESSED_CSV, index=False)
    print(f"✅ Processed signal saved locally to {PROCESSED_CSV}")