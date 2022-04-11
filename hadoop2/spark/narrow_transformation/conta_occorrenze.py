#!/usr/bin/env python3
import argparse

from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")
parser.add_argument("--output_path", type=str, help="Output folder path")

args = parser.parse_args()
input_filepath, output_filepath = args.input_path, args.output_path

spark = SparkSession \
    .builder \
    .appName("contatore sfide completate") \
    .getOrCreate()

input_RDD = spark.sparkContext.textFile(input_filepath).cache()


green_lines_RDD = input_RDD.filter(lambda line: 'green' in line)
orange_lines_RDD = input_RDD.filter(lambda line: 'orange' in line)


num_green = green_lines_RDD.count()
num_orange = orange_lines_RDD.count()


output_string = "sfide green: %i\nsfide orange: %i" % (num_green, num_orange)
spark.sparkContext.parallelize([output_string]) \
                  .saveAsTextFile(output_filepath)