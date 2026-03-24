import numpy as np
import pandas as pd
import os

# Project root (two levels up from src/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_CSV = os.path.join(PROJECT_ROOT, "signal.csv")

# Signal defaults
FREQ = 5
SAMPLE_RATE = 1000
DURATION = 1
NOISE_STD = 0.5
SEED = 42  # reproducible

def generate_signal(freq=FREQ, sample_rate=SAMPLE_RATE, duration=DURATION, noise_std=NOISE_STD, seed=SEED):
    if seed is not None:
        np.random.seed(seed)
    t = np.linspace(0, duration, sample_rate)
    signal = np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(0, noise_std, signal.shape)
    df = pd.DataFrame({"time": t, "amplitude": signal + noise})
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"✅ Signal generated locally: {OUTPUT_CSV}")
    return OUTPUT_CSV  # return path