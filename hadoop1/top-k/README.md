# Top - k


L'obiettivo è quello di recuperare le top-k entry in base a un qualche criterio<br>
In questo esempio si utilizza un file di ingresso composto da **n** righe e si produce un file di output di **k** righe.

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

Se k=2 e il criterio è il numero intero più alto l'output del sistema è il seguente.

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| d | 33  
| s | 22   
--- 

Si applica il _Top-k Pattern_.

**map** <br>
Scandise l'input ed effettua una pre-selezione dei top k. Restituisce in output tali entries.

**reduce** <br>
Riceve le top-k locali dai vari map tasks. Se si hanno n map task riceve in input n x k entries.<br>
Produce in output le top-k assolute.

