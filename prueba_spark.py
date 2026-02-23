import os, sys
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PruebaFinal").getOrCreate()

df = spark.createDataFrame([(1, "A"), (2, "B"), (3, "C")], ["id", "valor"])
print(df.collect())

spark.stop()
