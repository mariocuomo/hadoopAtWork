# Summarization


L'operazione di sommarizzazione permette di estrarre delle informazioni aggregative daò contenuto in input al sistema.<br>
In questo esempio si utilizza un file di ingresso composto da **n** righe e si produce un file di output di **m** (con m minore o uguale di n) righe.

Il file di input segue il seguente schema.

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| a | 2  
| d | 33 
| e | 1 
| a | 4
| s | 1 
| a | 3 
| s | 22 

Si vuole avere una informazione riguardo al numero totale di righe per ogni carattere.<br>
L'output del sistema sarà il seguente.

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| a | 3  
| d | 1 
| e | 1 
| s | 2
--- 

Si applica il _Summarization Pattern_.

**map** <br>
Scandise l'input e per ogni riga produce in output coppie che hanno la forma (carattere, 1)

**reduce** <br>
Riceve in input una lista di coppie (carattere, [1,1, ... ,1]) e produce in output coppie (carattere, len([1,1, ... ,1]))

