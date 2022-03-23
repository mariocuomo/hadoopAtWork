# Filter


L'operazione di filtro permette di filtrare il contenuto in input al sistema.<br>
In questo esempio si utilizza un file di ingresso composto da **n** righe e si produce un file di output di **m** (con m minore o uguale di n) righe.

Il file di input segue il seguente schema

| CARATTERE | NUMERO INTERO  
| :---: | :---: |
| a | 2  
| d | 33 
| e | 1 
| a | 1
| ... | ... 
| s | 26


Si vogliono recuperare tutte le righe del file che iniziano con la lettera 'a' e hanno associato un intero pari.

Si applica il _Filter Pattern_.

**map** <br>
Effettua il vero e proprio filtraggio. Si scandiscono le righe del file e si restituiscono in output le sole righe che soddisfano la condizione descritta in precedenza.

**reduce** <br>
Non effettua nessuna operazione, scrive le righe ricevute dalla map - più specificatamente dalla fase di _Shuffle and Sort_ - e le scrive sul file di output.

