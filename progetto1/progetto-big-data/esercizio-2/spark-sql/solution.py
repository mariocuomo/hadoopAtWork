#!/usr/bin/env python3
import argparse
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import split
from pyspark.sql.functions import collect_list
from pyspark.sql.functions import col
from pyspark.sql.functions import array
from heapq import nlargest
from operator import itemgetter



def prefered(x):
    lst=x[1]
    if len(lst)>5:
        return (x[0],nlargest(5, lst, key=itemgetter(1)))
    else:
        return (x[0],nlargest(len(lst), lst, key=itemgetter(1)))


parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")
parser.add_argument("--output_path", type=str, help="Output folder path")

args = parser.parse_args()
input_filepath, output_filepath = args.input_path, args.output_path

spark = SparkSession \
    .builder \
    .appName("prodotti preferiti di ogni utente") \
    .config("spark.executor.memory", "2000m") \
    .config("spark.memory.offHeap.size","16g") \
    .config("spark.memory.offHeap.enabled",True) \
    .getOrCreate()


input_df = spark.read.text(input_filepath).cache()
split_col = split(input_df['value'], '\t')

#(utente, prodotto, voto)
utente_prodotto_voto = input_df.withColumn('user', split_col.getItem(1)) \
                        .withColumn('prodotto', split_col.getItem(0)) \
                        .withColumn('voto', split_col.getItem(2).cast(IntegerType())) \
                        .drop("value")

#(utente, lista di prodottoVoto) 
utente_lista_prodottoVoto = utente_prodotto_voto.groupby("user").agg(collect_list(array("prodotto","voto")).alias('ProdottoVoto')) \
    .drop("prodotto") \
    .drop("voto")

#(utente, lista di prodottoVotoPreferiti)
utente_lista_preferiti = utente_lista_prodottoVoto.rdd.map(f=lambda x: prefered(x))

utente_lista_preferiti.saveAsTextFile(output_filepath)

spark.stop()