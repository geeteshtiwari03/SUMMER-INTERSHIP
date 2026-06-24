from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("SalesDataFrameAssignment") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Read CSV
df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

# --------------------------------------------------
# TASK 1
# Sort products by sales descending
# --------------------------------------------------

print("\n===== Products Sorted By Sales =====")

sorted_df = df.orderBy(
    col("sales").desc()
)

sorted_df.show()

# --------------------------------------------------
# TASK 2
# Top 3 Products
# --------------------------------------------------

print("\n===== Top 3 Products =====")

top3_df = sorted_df.limit(3)

top3_df.show()

# --------------------------------------------------
# TASK 3
# Filter sales > 80000
# --------------------------------------------------

high_sales_df = df.filter(
    col("sales") > 80000
)

high_sales_df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/high_sales_products")

print("\nFiltered products saved to output/high_sales_products")

spark.stop()