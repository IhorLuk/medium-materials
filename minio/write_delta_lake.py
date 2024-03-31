from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from delta import *

minio_access_key = "dev_user_01"
minio_secret_key = "devpassword01"
minio_end_point = "http://localhost:9000"

# start spark session with Delta Lake extensiouns
builder = SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder, extra_packages=["org.apache.hadoop:hadoop-aws:3.3.4"]).getOrCreate()

sc = spark.sparkContext
sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", "dev_user_01")
sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "devpassword01")
sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://localhost:9000")
sc._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
sc._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
sc._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
sc._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")

minio_bucket = "delta"

coffee_csv = 'coffee_sales.csv'
coffee_df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(coffee_csv)
file_count = coffee_df.count()

coffee_df.select(col("transaction_id"), col("transaction_date"), col("store_id"), col("store_location"), col("Total_Bill"), col("product_type")) \
    .write \
    .format("delta") \
    .partitionBy("store_location") \
    .mode("overwrite") \
    .save(f"s3a://{minio_bucket}/coffee-delta")

coffee_delta_read_df = spark.read.format("delta").load(f"s3a://{minio_bucket}/coffee-delta")
uploaded_count = coffee_delta_read_df.count()

if file_count == uploaded_count:
    print("All written correct!")
else:
    print("Some errors occured.")