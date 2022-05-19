#!/usr/bin/env python3
import argparse

from pyspark.sql import SparkSession
from collections import Counter
import os

def loadData(line):
    words=str(line).split("\t")
    return (words[3],words[4])



parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")

args = parser.parse_args()
input_filepath = args.input_path

spark = SparkSession \
    .builder \
    .appName("parole più usate per anno nelle recensioni") \
    .config("spark.executor.memory", "2000m") \
    .getOrCreate()

input_RDD = spark.sparkContext.textFile(input_filepath).cache()


# (anno, stringa)
anno_stringa_RDD = input_RDD.map(loadData)

# ((anno,parola))
anno_parola_RDD = anno_stringa_RDD.flatMap(lambda x: [(x[0],w) for w in x[1].split()])

# ((anno,parola),1)
anno_parola_uno_RDD = anno_parola_RDD.map(lambda x: ((x[0],x[1]),1))

# ((anno,parola),occorrenze)
anno_parole_occorrenze_RDD = anno_parola_uno_RDD.reduceByKey(func=lambda a,b: a+b)

# (anno,(parola,occorrenze))
anno_parole_occorrenze_swap_RDD = anno_parole_occorrenze_RDD.map(lambda x: (x[0][0],[[x[0][1],x[1]]]))

# (anno, lst(parola,occorrenze))
anno_lst_parole_occorrenze_RDD = anno_parole_occorrenze_swap_RDD.reduceByKey(func=lambda a,b: a+b)

# (anno, lst(parola,occorrenze))
anno_lst_parole_occorrenze_sortedTopK_RDD = anno_lst_parole_occorrenze_RDD.mapValues(f=lambda a: sorted(a,key = lambda x: x[1], reverse=True)[0:10])


dataset = anno_lst_parole_occorrenze_sortedTopK_RDD.collect()

with open('/home/mariocuomo/Desktop/progetto-big-data/esercizio-1/spark-core/output/output.txt', 'w+') as f:
    for anno,lst in dataset:
        f.write(anno+'\n')
        for parola, occorrenze in lst:
            f.write(parola+'\t'+str(occorrenze)+'\n')
        f.write('\n')
