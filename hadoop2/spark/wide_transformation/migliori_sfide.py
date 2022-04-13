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


sfida_speed_memory_RDD = input_RDD.map(f=lambda line: line.split("\t"))


sorted_speed_RDD = sfida_speed_memory_RDD.sortBy(
    keyfunc=lambda sfida_speed_memory : sfida_speed_memory[1],
    ascending=False)

sorted_memory_RDD = sfida_speed_memory_RDD.sortBy(
    keyfunc=lambda sfida_speed_memory : sfida_speed_memory[2],
    ascending=False)


top_speed = sorted_speed_RDD.take(3)
top_memory = sorted_memory_RDD.take(3)


output_string = "MIGLIORI SFIDA PER VELOCITA\n"
for [sfida,velocita,memoria] in top_speed:
    output_string=output_string+sfida+", velocita:  "+velocita+'\n'

output_string = output_string+"\n\nMIGLIORI SFIDA PER MEMORIA\n"
for [sfida,velocita,memoria] in top_memory:
    output_string=output_string+sfida+", memoria:  "+memoria+'\n'


spark.sparkContext.parallelize([output_string]) \
                  .saveAsTextFile(output_filepath)