-- Start psql and connect to the default database
psql -U your_username

-- Create a new database named traffic_data
CREATE DATABASE traffic_data;

-- Connect to the newly created database
\c traffic_data

-- Create a table within the traffic_data database
CREATE TABLE traffic_summary (
    sensor_id VARCHAR(50),
    average_speed FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
