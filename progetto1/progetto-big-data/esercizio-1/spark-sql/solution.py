#!/usr/bin/env python3

import argparse
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import split
from pyspark.sql.functions import collect_list
from pyspark.sql.functions import concat_ws
from collections import Counter
from pyspark.sql.functions import col

def most_used(x):
    lst = x.split(" ")
    lst_occ = list(Counter(lst).most_common(10))

    s = ""
    for item in lst_occ:
        s = s+ str(item[0])+' '+str(item[1])+';'
    return s
    


parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")
parser.add_argument("--output_path", type=str, help="Output folder path")

args = parser.parse_args()
input_filepath, output_filepath = args.input_path, args.output_path

spark = SparkSession \
    .builder \
    .appName("parole più usate per anno nelle recensioni") \
    .config("spark.executor.memory", "2000m") \
    .config("spark.memory.offHeap.size","16g") \
    .config("spark.memory.offHeap.enabled",True) \
    .getOrCreate() \

input_df = spark.read.text(input_filepath).cache()
split_col = split(input_df['value'], '\t')


#(anno, recensione)
anno_recensione = input_df.withColumn('anno', split_col.getItem(3).cast(IntegerType())) \
                        .withColumn('recensione', split_col.getItem(4)) \
                        .drop("value")

#(anno, stringa di tutte le recensioni)
anno_recensioni = anno_recensione.groupby("anno").agg(concat_ws(" ", collect_list(anno_recensione.recensione)))
anno_recensioni = anno_recensioni.withColumnRenamed("anno","recensione")

#(anno, stringa delle 10 parole piu usate con forma 'parola occorrenze; parola occorrenze; ...')
anno_paroleTop = anno_recensioni.rdd.map(lambda x: (x[0],most_used(x[1])))


anno_paroleTop.saveAsTextFile(output_filepath)

spark.stop()
