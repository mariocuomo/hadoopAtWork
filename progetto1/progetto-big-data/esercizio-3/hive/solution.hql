CREATE TABLE info (ProductId STRING, UserId STRING, Score STRING, Timee STRING, Textt STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

ADD FILE /home/mariocuomo/Desktop/progetto-big-data/esercizio-3/hive/listAgg.py;

LOAD DATA LOCAL INPATH '/home/mariocuomo/Desktop/progetto-big-data/datasets/ReviewsPulitoN.txt'
OVERWRITE INTO TABLE info;


CREATE TABLE info_join_info AS
SELECT i.UserId as Utente1, i1.UserId as Utente2, i.ProductId as ProductId
FROM info i
INNER JOIN info i1 
ON i.ProductId = i1.ProductId
AND i.UserId < i1.UserId
WHERE i.Score>=4 AND i1.Score>=4;

/*per avere coppie (x,y) e (y,x) ---- AND i.UserId <> i1.UserId*/

CREATE TABLE affini AS
WITH coppie AS (
SELECT Utente1, Utente2, Count(*) as recensioni_comuni
FROM info_join_info
GROUP BY Utente1, Utente2
)
SELECT Utente1,Utente2
FROM coppie
WHERE recensioni_comuni >= 3;


CREATE TABLE info_join_info_affini AS
SELECT * FROM info_join_info
WHERE EXISTS
(SELECT * FROM affini WHERE affini.Utente1=info_join_info.Utente1 and affini.Utente2=info_join_info.Utente2);


CREATE TABLE resultList AS
WITH cte AS (SELECT * FROM info_join_info_affini ORDER BY Utente1)
SELECT TRANSFORM(cte.Utente1, cte.Utente2, cte.ProductId)
USING 'python3 /home/mariocuomo/Desktop/progetto-big-data/esercizio-3/hive/listAgg.py'
FROM cte;


SELECT * FROM resultList LIMIT 10;

DROP TABLE info;
DROP TABLE info_join_info;
DROP TABLE affini;
DROP TABLE info_join_info_affini;

INSERT OVERWRITE LOCAL DIRECTORY '/home/mariocuomo/Desktop/progetto-big-data/esercizio-3/hive/output' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM resultList;

DROP TABLE resultList;


