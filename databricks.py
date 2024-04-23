# Databricks notebook source
from pyspark.sql import *
from pyspark import SparkContext, SparkConf
from pyspark.sql.functions import *
from pyspark.sql.types import *


# COMMAND ----------

spark = SparkSession.builder.appName("databricks").getOrCreate()

# COMMAND ----------

spark

# COMMAND ----------


