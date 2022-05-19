#!/usr/bin/env python3
import argparse
from pyspark.sql import SparkSession
import itertools


def loadData(line):
    words=str(line).split("\t")
    return (words[0],words[1],words[2])

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")

args = parser.parse_args()
input_filepath = args.input_path

spark = SparkSession \
    .builder \
    .appName("coppie di utenti affini") \
    .getOrCreate()

input_RDD = spark.sparkContext.textFile(input_filepath).cache()

# (prodotto, user,voto)
tutti_campi_RDD = input_RDD.map(loadData)
tutti_campi_RDD = tutti_campi_RDD.filter(lambda x: int(x[2]) >=5)


# (prodotto, user)
prodotto_utente_RDD = tutti_campi_RDD.map(f=lambda line: (line[0], [line[1]]))


# (prodotto, lista utenti)
prodotto_lstutenti_RDD = prodotto_utente_RDD.reduceByKey(func=lambda a,b: a+b)

# ([user1,user2],prodotto)
# (prodotto, lista_di_tutte_le_coppie_user1_user2) ->   swap di (prodotto, [user1,user2] ) ->   ([user1,user2],prodotto)
utente1_utente2_prodotto =  prodotto_lstutenti_RDD.mapValues(f=lambda a: list(itertools.combinations(a, 2))).flatMap(lambda x: [(w,[x[0]]) for w in x[1]])

# ([user1,user2],lista prodotti)
utente1_utente2_prodotti = utente1_utente2_prodotto.reduceByKey(func=lambda a,b: a+b).filter(lambda x: len(x[1]) >=3)

# (user1,user2,lista prodotti)
utente1_utente2_prodotti=utente1_utente2_prodotti.map(f=lambda line: (line[0][0], line[0][1], line[1]))


dataset = utente1_utente2_prodotti.collect()
dataset.sort(key=lambda x: x[0])

with open('/home/mariocuomo/Desktop/progetto-big-data/esercizio-3/spark-core/output/output.txt', 'w+') as f:
    for utente1,utente2,lst in dataset:
        f.write(utente1+' e '+utente2+'\n')
        for prodotto in lst:
            f.write(prodotto+'\n')
        f.write('\n')



