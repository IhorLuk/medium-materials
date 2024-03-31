from pyspark.sql import SparkSession
from pyspark.sql.functions import col

bucket_name = "test-bucket"

# start spark session
spark = SparkSession.builder \
    .appName('parquet-load') \
    .getOrCreate()

sc = spark.sparkContext

# specify configurations for hadoop
# Note - you should have aws hadoop installed
sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", "dev_user_01")
sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "devpassword01")
sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://localhost:9000")
sc._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
sc._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
sc._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
sc._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")

# read csv file and write it to the MiniO
coffee_csv = 'coffee_sales.csv'
coffee_df = spark.read.format('csv').option('header', 'true').load(coffee_csv)
coffee_df \
    .write \
    .mode("overwrite") \
    .parquet(f"s3a://{bucket_name}/coffee_sales.parquet")