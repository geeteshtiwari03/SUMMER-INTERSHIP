from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PartitionAssignment") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")


df = spark.range(5000000)

print("\n===== Initial Partitions =====")

initial_partitions = df.rdd.getNumPartitions()

print(initial_partitions)


df_repartitioned = df.repartition(12)

print("\n===== After Repartition(12) =====")

print(df_repartitioned.rdd.getNumPartitions())


df_coalesced = df_repartitioned.coalesce(3)

print("\n===== After Coalesce(3) =====")

print(df_coalesced.rdd.getNumPartitions())

spark.stop()