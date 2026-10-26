
-- PostgreSQL schema design for a future renewable-energy forecasting system.

-- NOTE:
-- This schema models how production telemetry data could be stored.
-- The current project uses simulated telemetry generated through the ETL pipeline.
-- Real weather, generation, and demand datasets will be integrated in future versions.

-- =========================================================
-- Table: stations
--
-- Stores metadata for energy-generation assets such as
-- wind farms, solar parks, or battery facilities.

CREATE TABLE stations (
    station_id SERIAL PRIMARY KEY,
    station_name VARCHAR(100) NOT NULL,
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL,
    capacity_mw DECIMAL(8, 2) NOT NULL
);

CREATE TABLE grid_telemetry (
    record_id SERIAL PRIMARY KEY,
    station_id INT REFERENCES stations (station_id),
    timestamp TIMESTAMPTZ NOT NULL,
    temperature_c DECIMAL(5, 2),
    ghi_w_m2 DECIMAL(7, 2), -- Global Horizontal Irradiance (Solar)
    wind_speed_ms DECIMAL(5, 2), -- Wind speed in m/s
    actual_generation_mw DECIMAL(8, 2) -- Target variable
);
