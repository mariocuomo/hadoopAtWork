# Join


L'operazione di join permette di recuperare informazioni associando quelle memorizzate su diversi file di input in base a un qualche parametro comune<br>
In questo esempio si hanno in input due file composti rispettivamente da **n** e **m** righe ciascuno. Il file in output ha al più **m x n** righe.

Il fileA di input segue il seguente schema.

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| a | 2  
| d | 33 
| e | 1 
| a | 4
| s | 1 
| a | 3 

Il fileB di input segue il seguente schema.

| CARATTERE | CODICE
| :---: | :---: |
| a | 68a51  
| d | 32a54
| c | 98e2 
| l | 32r22
| f | 3v32

Si vuole effettuare il join sulla condizione fileA.carattere==fileB.carattere<br>

--- 

Si applica il _Join Pattern_.

**map** <br>
Scorre entrambi file producendo in output coppie (valore_di_join, informazione, fileDiProvenienza)

**reduce** <br>
Per ogni valore di join raggruppa le informazioni provenienti dai due file differenti creando una struttura del tipo (valore_di_join, [(info,file), (info,file)]). Effettua il prodotto cartesiano tra le informazioni provenienti da file differenti.

