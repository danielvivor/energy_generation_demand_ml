# =========================================================
# Environment Configuration
# =========================================================

import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# =========================================================
# Third-Party Libraries
# =========================================================

import pandas as pd
from sqlalchemy import create_engine

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# =========================================================
# Database Connection
# =========================================================

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Pull clean data from database
query = "SELECT temperature_c, ghi_w_m2, wind_speed_ms, temp_rolling_3h, wind_lag_1h, actual_generation_mw FROM grid_telemetry_clean"
df = pd.read_sql(query, engine)

# =========================================================
# Feature Selection
#
# Define the predictor variables (X) and the target
# variable (y) for machine-learning training.
#
# X:
#     Weather and engineered telemetry features.
#
# y:
#     Actual power generation output to be predicted.
# ========================================================= 

X = df[['temperature_c', 'ghi_w_m2', 'wind_speed_ms', 'temp_rolling_3h', 'wind_lag_1h']]
Y = df['actual_generation_mw']

# Train/ Test Split (respecting chronological order is best practice for time-series)
# Determine the training dataset size.
train_size = int(len(df) * 0.8)

# Historical data used for model training.
X_train = X.iloc[:train_size]
Y_train = Y.iloc[:train_size]

# Future data used for model evaluation.
X_test = X.iloc[train_size:]
Y_test = Y.iloc[train_size:]
