# Distinct


L'operazione di distinct permette di eliminare i duplicati delle righe del file di input<br>
In questo esempio si utilizza un file di ingresso composto da **n** righe e si produce un file di output di **m** righe (con m minore o uguale di n) righe.

Il file di input segue il seguente schema.

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| a | 2  
| d | 33 
| e | 6 
| e | 6
| s | 1 
| a | 3 
| a | 2 

Si vuole ordinare le righe in maniera crescente sulla base del numero intero associato.<br>
L'output del sistema sarà il seguente.

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| a | 2  
| d | 33  
| e | 6 
| s | 1 
| a | 3
--- 

Si applica il _Distinct Pattern_.

**map** <br>
Scandise l'input e per ogni riga produce in output coppie che hanno la forma (riga, valore_nullo)

**reduce** <br>
Riceve in input una lista di coppie (riga, [null,null, ... ,null]) e produce in output la chiave riga.

