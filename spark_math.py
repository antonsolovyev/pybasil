from __future__ import print_function

import random

from pyspark.sql import SparkSession


if __name__ == '__main__':
    spark = SparkSession.builder.master('spark://white.home:7077').appName("Math on Spark").getOrCreate()

    def f(pair):
        return pair[0] + pair[1]

    pairs = []
    for i in range(0, 1000000):
        pairs.append((random.randint(0, 77), random.randint(0, 33)))

    sums = spark.sparkContext.parallelize(pairs, 4).map(f).collect()

    # for p in pairs:
    #     print('left: %s, right %s' % (p[0], p[1]))
    # for s in sums:
    #     print('s: %s' % s)
    print('count: %s' % len(sums))

    spark.stop()
