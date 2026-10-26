
-- Validation Queries

-- Purpose:
-- Used to verify that tables were created successfully
-- and contain the expected data.

-- These queries are intended for development and testing.
-- =========================================================

-- View all registered energy-generation stations.
SELECT * FROM stations;

-- View all telemetry and weather observations.
SELECT * FROM grid_telemetry;