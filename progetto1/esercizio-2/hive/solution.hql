CREATE TABLE info (ProductId STRING, UserId STRING, Score STRING, Timee STRING, Textt STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

ADD FILE /home/mariocuomo/Desktop/progetto-big-data/esercizio-2/hive/listAgg.py;

LOAD DATA LOCAL INPATH '/home/mariocuomo/Desktop/progetto-big-data/datasets/ReviewsPulitoN.txt'
OVERWRITE INTO TABLE info;


CREATE TABLE result AS
	WITH cte AS (
		SELECT UserId, Score, ProductId, ROW_NUMBER() OVER (PARTITION BY UserId ORDER BY Score DESC) AS rn
		FROM info
		)
	SELECT UserId,Score,ProductId
	FROM cte
	WHERE rn <= 5
	ORDER BY Score DESC;



CREATE TABLE resultList AS
WITH cte AS (SELECT * FROM result ORDER BY UserId)
SELECT TRANSFORM(cte.UserId, cte.Score, cte.ProductId)
USING 'python3 /home/mariocuomo/Desktop/progetto-big-data/esercizio-2/hive/listAgg.py'
FROM cte;


DROP TABLE info;
DROP TABLE result;

INSERT OVERWRITE LOCAL DIRECTORY '/home/mariocuomo/Desktop/progetto-big-data/esercizio-2/hive/output' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM resultList;

DROP TABLE resultList;


