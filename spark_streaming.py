from kafka import KafkaProducer
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import Structtype, StructField, StringType, IntegerType, FloatType

# Initialize spark session
spark = SparkSession.builder \
    .appName("TrafficDataProcessing") \
    .getOrCreate()

# Define schema for incoming JSON data
schema = StructType([
    StructField("sensor_id", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("vehicle_count", IntegerType(), True),
    StructField("average_speed", FloatType(), True),
    StructField("incident", StringType(), True)
])

# Read data from kafka
traffic_data = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "traffic_data") \
    .load()

# Parse JSON data
