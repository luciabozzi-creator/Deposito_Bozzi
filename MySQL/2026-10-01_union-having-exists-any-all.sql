-- ESERCIZIO UNION, HAVING, EXISTS, ANY, ALL
/*
Le due tabelle sono collegate dalla relazione tra Clienti.id e Ordini.id_cliente.

Si considerino le seguenti due tabelle con 20 dati l’una:

Clienti (
id INT,
nome VARCHAR(100),
città VARCHAR(100)
)

Ordini (
id INT,
id_cliente INT,
data_ordine DATE,
importo DECIMAL(7,2)
)
*/

-- 
-- SELECT * FROM Clienti;

-- UNION e UNION ALL :
-- Visualizza l'elenco delle città in cui sono presenti clienti unendolo a una lista di città target, 
-- prima rimuovendo i duplicati e successivamente mantenendoli tutti.

SELECT citta
FROM Clienti
UNION -- qui si appiattiscono i duplicati
SELECT 'AA Città Nuova Target da aggiungere in elenco'
ORDER BY citta ASC; 

SELECT citta
FROM Clienti
UNION ALL -- qui rimangono i duplicati
SELECT 'AA Città Nuova Target da aggiungere in elenco'
ORDER BY citta ASC; 

-- HAVING :
-- Visualizza l'elenco dei clienti che hanno effettuato una spesa totale complessiva superiore a 1.000€.
-- Mostra per ciascuno: id_cliente e totale speso.



-- EXISTS :
-- Visualizza tutti i clienti che hanno registrato almeno un ordine nel sistema.
-- Mostra per ciascuno: id e nome del cliente.


-- ANY e ALL :
-- Visualizza gli ordini con importo superiore ad almeno un ordine (ANY) o a tutti gli ordini (ALL) effettuati dai clienti di una specifica città.
-- Mostra per ciascuno: id dell'ordine e importo.