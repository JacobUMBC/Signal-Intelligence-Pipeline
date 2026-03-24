# src/signal_pipeline.py
from datetime import datetime
import os

from src.signal_generator.generator import generate_signal
from src.processing.fft_processor import run_fft_processor
from src.detection.anomaly_detector import run_anomaly_detector
from src.db.db_connector import push_to_db

# Force local mode
os.environ['S3_RAW_BUCKET'] = ''
os.environ['S3_PROCESSED_BUCKET'] = ''
os.environ['S3_ANOMALY_BUCKET'] = ''

# Files to remove at start
CSV_FILES = ["signal.csv", "processed_signal.csv", "anomalies.csv"]

def clean_old_csvs():
    for file in CSV_FILES:
        if os.path.exists(file):
            os.remove(file)
            print(f"🗑️ Removed old file: {file}")

def main():
    print("=======================================")
    print(f"📅 Starting Signal Pipeline at {datetime.now()}")
    print("=======================================\n")

    # Clean old CSVs
    clean_old_csvs()

    # 0️⃣ Generate raw signal
    print("🔹 Generating raw signal...")
    generate_signal()
    print("✅ Signal generation completed\n")

    # 1️⃣ FFT Processing
    print("🔹 Running FFT Processing...")
    run_fft_processor()
    print("✅ FFT Processing Completed\n")

    # 2️⃣ Anomaly Detection
    print("🔹 Running Anomaly Detection...")
    run_anomaly_detector()
    print("✅ Anomaly Detection Completed\n")

    # 3️⃣ Push to DB
    print("🔹 Pushing results to PostgreSQL...")
    push_to_db()
    print("✅ Data successfully pushed to DB\n")

    print("=======================================")
    print("🎉 Signal Pipeline Completed!")
    print("=======================================")

if __name__ == "__main__":
    main()