# Sorting


L'operazione di sorting permette di ordinare le righe del file di input in base a un qualche criterio<br>
In questo esempio si utilizza un file di ingresso composto da **n** righe e si produce un file di output di **n**.

Il file di input segue il seguente schema.

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| a | 2  
| d | 33 
| e | 6 
| a | 4
| s | 1 
| a | 3 
| s | 22 

Si vuole ordinare le righe in maniera crescente sulla base del numero intero associato.<br>
L'output del sistema sarà il seguente.

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| s | 1  
| a | 2  
| a | 3 
| a | 4 
| e | 5
| s | 22 
| d | 33 
--- 

Si applica il _Sorting Pattern_.

**map** <br>
Scandise l'input e per ogni riga produce in output coppie che hanno la forma (numero intero, riga completa)

**reduce** <br>
Riceve in input una lista di coppie (numero intero, [riga,riga, ... ,riga]) e produce in output le righe.

L'ordinamento è effettuato dal sistema durante la fase di _Shuffle and Sort_ - operazione eseguita quando terminano i map jobs e prima che iniziano i reduce jobs.

