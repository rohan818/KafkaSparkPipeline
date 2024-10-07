# Kafka-Spark-Pipeline


## Prerequisites

- Install Apache Kafka and Apache Spark.
- Ensure you have Java installed beforehand.

### Python Libraries

It is advised to create a Python virtual environment in your project directory and then install the required libraries:

```bash
pip install kafka-python
pip install pyspark
```

## Execution Steps

1. **Start Zookeeper**

   Navigate to the Kafka directory and start Zookeeper:

   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```

2. **Start Kafka Server**

   In a new terminal window, start the Kafka server:

   ```bash
   bin/kafka-server-start.sh config/server.properties
   ```

3. **Create a Kafka Topic**

   Create a Kafka topic, say, 'traffic_data':

   ```bash
   bin/kafka-topics.sh --create --topic traffic_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

4. **Run Data Simulation Script**

   Run the `data_simulation.py` script. This initializes a Kafka producer and simulates continuous generation of traffic sensor data:

   ```bash
   python data_simulation.py
   ```

5. **Run Spark Streaming Application**

   Execute the `spark_streaming.py` script using `spark-submit`:

   ```bash
   spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 kafkaSparkPipeline/spark_streaming.py
   ```