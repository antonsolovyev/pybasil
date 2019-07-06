from __future__ import print_function

from random import random
from operator import add

from pyspark.sql import SparkSession


if __name__ == '__main__':
    spark = SparkSession.builder.master('spark://white.home:7077').appName("PI on Spark").getOrCreate()

    partitions = 30
    n = 1000000 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    print('PI is roughly %f' % (4.0 * count / n))

    spark.stop()
