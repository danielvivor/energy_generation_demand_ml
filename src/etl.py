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

# Introduce artificial missing values (sensor dropouts) to simulate data cleaning
raw_data.loc[50:55, "temperature_c"] = np.nan
raw_data.loc[200:205, "wind_speed_ms"] = np.nan

# =========================================================
# Time-Series Preparation
#
# Convert timestamp values into Pandas datetime objects,
# then use the timestamp column as the DataFrame index.
#
# A datetime index enables time-based operations such as:
# - interpolation
# - rolling windows
# - resampling
# - forecasting workflows
# =========================================================
# 2. Pandas cleaning & Feature engineering
# Convert timestamps to datetime objects.
raw_data["timestamp"] = pd.to_datetime(raw_data["timestamp"])

# Use timestamps as the DataFrame index and ensure
# observations are ordered chronologically.
raw_data = raw_data.set_index("timestamp").sort_index()

# Estimate missing temperature observations.
raw_data["temperature_c"] = raw_data["temperature_c"].interpolate(method="time")

# Estimate missing wind-speed observations.
raw_data["wind_speed_ms"] = raw_data["wind_speed_ms"].interpolate(method="time")

# =========================================================
# Feature Engineering

# Rolling features capture recent trends while lag features
# provide historical context for the machine-learning model.
# =========================================================

# Average temperature over the previous 3-hour period.
raw_data["temp_rolling_3h"] = raw_data["temperature_c"].rolling(window="3h").mean()

# Wind speed observed one hour earlier.
raw_data["wind_lag_1h"] = raw_data["wind_speed_ms"].shift(1)

# Drop any remaining initialization NaNs from lagging/rolling
cleaned_data = raw_data.dropna().reset_index()

# =========================================================
# Inspect the final dataset before loading it into PostgreSQL.
#
# Validation checks:
# - Preview transformed records
# - Confirm expected dataset dimensions
# - Verify that no missing values remain
# =========================================================

print("\nDataset Preview:")
print(cleaned_data.head())

print("\nShape:")
print(cleaned_data.shape)

print("\nMissing Values:")
print(cleaned_data.isna().sum())

# 3. Load into PostgreSQL (using SQLAlchemy and psycopg backend)
engine = create_engine(
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
cleaned_data.to_sql("grid_telemetry_clean", engine, if_exists="append", index=False)
