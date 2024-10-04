from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# List of sensors
sensor_ids = ['sensor_1', 'sensor_2', 'sensor_3']

def generate_traffic_data():
    while True:
        # Simulate data for each sensor
        for sensor_id in sensor_ids:
            data = {
                'sensor_id': sensor_id,
                'timestamp': datetime.now().isoformat(),
                'vehicle_count': random.randint(0, 20),
                'average_speed': round(random.uniform(20.0, 80.0), 2),
                'incident': random.choice(['None', 'Accident', 'Roadblock'])
            }
            # send data to kafka topic
            producer.send('traffic_data', value=data)
            print(f"Sent: {data}")

        # wait 1 second before sending next batch
        time.sleep(1)

if __name__ == "__main__":
    generate_traffic_data()