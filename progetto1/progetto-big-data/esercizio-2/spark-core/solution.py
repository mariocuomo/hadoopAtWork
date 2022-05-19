#!/usr/bin/env python3
import argparse

from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")

args = parser.parse_args()
input_filepath = args.input_path

spark = SparkSession \
    .builder \
    .appName("prodotti preferiti di ogni utente") \
    .getOrCreate()

input_RDD = spark.sparkContext.textFile(input_filepath).cache()

tutti_campi_RDD = input_RDD.map(f=lambda line: line.split("\t"))
utente_prodotto_voto_RDD = tutti_campi_RDD.map(f=lambda line: (line[1],[[line[0], line[2]]]))


utente_lista_prodotti_voti_RDD = utente_prodotto_voto_RDD.reduceByKey(func=lambda a,b: a+b)

utente_lista_prodotti_voti_ordinati_RDD = utente_lista_prodotti_voti_RDD.map(f=lambda a: (a[0], sorted(a[1],y = lambda x: x[1], reverse=True)) )


utente_lista_prodotti_voti_topK = utente_lista_prodotti_voti_RDD.map(f=lambda a: (a[0], a[1][0:5]))

utente_lista_prodotti_voti_sorted = utente_lista_prodotti_voti_topK.sortBy(keyfunc=lambda a: a[0])

dataset = utente_lista_prodotti_voti_sorted.collect()

with open('/home/mariocuomo/Desktop/progetto-big-data/esercizio-2/spark-core/output/output.txt', 'w+') as f:
    for utente,lst in dataset:
        f.write(utente+'\n')
        for prodotto, voto in lst:
            f.write(prodotto+'\t'+str(voto)+'\n')
        f.write('\n')
