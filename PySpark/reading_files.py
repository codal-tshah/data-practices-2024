# -*- coding: utf-8 -*-
"""Reading_Files.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wF07Y8y_fCQH_2Ihq7LOEYfY4VSjjLFI
"""

from google.colab import drive

drive.mount("/content/drive")

# !pip install pyspark

from pyspark import *
from pyspark.sql import DataFrame

help(DataFrame.write)

from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext("local")
spark = SparkSession(sc)

data = [(1, "milan", 56), (2, "rahul", 26), (3, "mihir", 34), (4, "jay", 21)]
schema = ["id", "name", "age"]
df = spark.createDataFrame(data=data, schema=schema)
df.show()

display(df)

df.write

type(df.write)

"""# **Read CSV FILE**"""

df.write.csv(
    path="/content/drive/MyDrive/data_practices/pyspark/data/csv_2", header=True
)

df = spark.read.csv(
    path="/content/drive/MyDrive/data_practices/pyspark/data/csv_2", header=True
)
df.show()

display(
    spark.read.csv(
        path="/content/drive/MyDrive/data_practices/pyspark/data/csv_2", header=True
    )
)

df.write.csv(
    path="/content/drive/MyDrive/data_practices/pyspark/data/csv_1",
    header=True,
    mode="error",
)

help(df.write.csv)

df.write.csv(
    path="/content/drive/MyDrive/data_practices/pyspark/data/csv_1",
    header=True,
    mode="overwrite",
)
df = spark.read.csv(
    path="/content/drive/MyDrive/data_practices/pyspark/data/csv_1", header=True
)
df.show()

df.write.csv(
    path="/content/drive/MyDrive/data_practices/pyspark/data/csv_1",
    header=True,
    mode="append",
)
df = spark.read.csv(
    path="/content/drive/MyDrive/data_practices/pyspark/data/csv_1", header=True
)
df.show()

"""# **Read JSON FILE**"""

dj = spark.read.json(
    "/content/drive/MyDrive/data_practices/pyspark/data/file1.json", multiLine=True
)
dj.show()

dj.printSchema()

dj = spark.read.json(
    path="/content/drive/MyDrive/data_practices/pyspark/data/file1.json", multiLine=True
)
dj.show()

"""Multiple Json files reading"""

multi_json = spark.read.json(
    path="/content/drive/MyDrive/data_practices/pyspark/data/*.json", multiLine=True
)
multi_json.show()

multi_json = spark.read.json(
    path=[
        "/content/drive/MyDrive/data_practices/pyspark/data/file1.json",
        "/content/drive/MyDrive/data_practices/pyspark/data/sample4.json",
    ],
    multiLine=True,
)
multi_json.show()

multi_json = spark.read.json(
    path="/content/drive/MyDrive/data_practices/pyspark/data/sample4.json",
    multiLine=True,
)
multi_json.show()

multi_json = spark.read.json(
    path=[
        "/content/drive/MyDrive/data_practices/pyspark/data/sample4.json",
        "/content/drive/MyDrive/data_practices/pyspark/data/file1.json",
    ],
    multiLine=True,
)
multi_json.show()

multi_json = spark.read.json(
    path=[
        "/content/drive/MyDrive/data_practices/pyspark/data/sample4.json",
        "/content/drive/MyDrive/data_practices/pyspark/data/new.json",
    ],
    multiLine=True,
)
multi_json.show()

multi_json.printSchema()

"""Write DataFrame into Json"""

wt = [(1, "milan", 56), (2, "rahul", 26), (3, "mihir", 34), (4, "jay", 21)]
schema = ["id", "name", "age"]
wd = spark.createDataFrame(data=wt, schema=schema)
wd.show()

wd.write.json("/content/drive/MyDrive/data_practices/pyspark/data/js")
wd.show()

wd.write.json("/content/drive/MyDrive/data_practices/pyspark/data/js", mode="append")
wd.show()

wd.write.json("/content/drive/MyDrive/data_practices/pyspark/data/js", mode="overwrite")
wd.show()
