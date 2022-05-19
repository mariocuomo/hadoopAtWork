import org.apache.spark.sql.functions._
import org.apache.spark.sql.Row

val startTimeMillis = System.currentTimeMillis()

val input_df = spark.read.option("sep", "\t").option("header", "false").csv("file:///home/mariocuomo/Desktop/progetto-big-data/datasets/ReviewsPulitoN.txt")


// (prodotto, utente, voto, tempo, recensione)
val newColumns = Seq("prodotto","user","voto", "tempo", "recensione")
val df = input_df.toDF(newColumns:_*)

// (prodotto, utente)
val df_filtrato = df.filter(df("voto") >3).drop("voto").drop("tempo").drop("recensione")


// (prodotto, utente1, prodotto2, utente2)
val p_u_p_u = 
	df_filtrato.as("u1").withColumnRenamed("user", "user1").
    join(
    	df_filtrato.as("u2").withColumnRenamed("user", "user2"),$"u1.prodotto" === $"u2.prodotto")

// (prodotto, utente1, prodotto2)
val newColumns = Seq("prodotto","user1","prodotto2", "user2")
val prodotto_utente_utente = p_u_p_u.toDF(newColumns:_*).drop("prodotto2").filter($"user1" !== $"user2")


// (utente1, prodotto2, lista_prodotti)
val utente1_utente2_lst = prodotto_utente_utente.groupBy($"user1", $"user2").agg(collect_list("prodotto"))
val newColumns = Seq("user1","user2","prodotti")
val utente1_utente2_listaProdotti = utente1_utente2_lst.toDF(newColumns:_*).filter(size($"prodotti")>=3)



utente1_utente2_listaProdotti.withColumn("prodotti", $"prodotti".cast("string")).write.format("csv").save("file:////home/mariocuomo/Desktop/progetto-big-data/esercizio-3/spark-sql/output.csv")

val endTimeMillis = System.currentTimeMillis()
val durationSeconds = (endTimeMillis - startTimeMillis) / 1000