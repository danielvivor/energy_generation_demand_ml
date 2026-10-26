# Environment Configuration
#
# Loads PostgreSQL connection settings from a local .env
# file so credentials are not stored directly in source
# code or committed to GitHub.
# =========================================================

import os
from dotenv import load_dotenv

# Load environmental variables from the .env file.
load_dotenv()

# Database connection settings.
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# 1.Simulate raw incoming time-series data (e.g., hourly records for a solar/wind park)
# Generate 30 days of hourly timestamps for simulated telemetry data.
date_range = pd.date_range(start="2026-01-01", periods=720, freq="h")
np.random.seed(42)

raw_data = pd.DataFrame(
    {
        "timestamp": date_range,
        "station_id": 1,
        "ghi_w_m2": np.maximum(
            0, np.sin(np.linspace(0, 50, 720)) * 800 + np.random.normal(0, 50, 720)
        ),
        "wind_speed_ms": np.random.uniform(10, 4, size=720),
        "actual_generation_mw": np.random.uniform(0, 50, size=720),
    }
)
