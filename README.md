# Renewable Energy Generation & Demand Forecasting
Power grids must match supply and demand in real time. Because solar and wind generation depend on weather, utility platforms rely heavily on automated time-series forecasting to prevent blackout risks and reduce grid inefficiency.

A project exploring renewable energy generation and demand forecasting using:

- PostgreSQL
- Pandas
- NumPy
- Scikit-Learn

## Current Progress

### ✅ Completed

### 🚧 In Progress
- PostgreSQL database setup
- ETL pipeline
- Data cleaning
- Feature engineering
- Random Forest forecasting model
- Model evaluation using RMSE

- Integration of real German energy datasets
- Improved forecasting models
- Time-series validation

## Tech Stack

- Python
- PostgreSQL
- Pandas
- NumPy
- SQLAlchemy
- Scikit-Learn

## Project Architecture

```text
Raw Data
    ↓
ETL Pipeline
    ↓
PostgreSQL
    ↓
Machine Learning
    ↓
Forecasts
```

## Project Goals

This project aims to build an end-to-end renewable energy forecasting workflow that:

- Ingests energy and weather data
- Cleans and transforms raw telemetry
- Stores processed data in PostgreSQL
- Trains machine-learning models for forecasting
- Evaluates model performance using industry-standard metrics
- Evolves towards real-world energy and weather datasets

## Version History

### Version 1.0

- Simulated renewable energy telemetry generation
- ETL pipeline with Pandas
- Feature engineering:
  - Rolling temperature averages
  - Lagged wind-speed features
- PostgreSQL integration
- Random Forest baseline forecasting model
- RMSE-based evaluation

## Next Steps

- Integrate real German weather data (DWD)
- Integrate real German energy generation and demand datasets
- Compare Random Forest against additional models
- Implement proper time-series cross-validation
- Add visualisations and forecasting dashboards
- Develop a web-based interface for forecast monitoring