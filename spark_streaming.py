from kafka import KafkaProducer
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

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
traffic_df = traffic_data.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Process data, here calculating avg. speed per sensor
processed_data = traffic_df.groupBy("sensor_id") \
    .avg("average_speed") \
    .alias("average_speed")

# Function to write to PostgreSQL
def write_to_postgres(df, epoch_id):
    df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/traffic_data") \
    .option("dbtable", "traffic_summary") \
    .option("user", "") \
    .option("password", "") \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()

# Output to PostgreSQL
query = processed_data.writeStream \
    .foreachBatch(write_to_postgres) \
    .outputMode("update") \
    .start()

'''
# Output to console
query = processed_data.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()
'''

query.awaitTermination()