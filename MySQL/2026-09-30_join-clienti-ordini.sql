-- ESERCIZIO JOIN --
/*
Si considerino le seguenti due tabelle con 20 dati l'una:
Clienti (
    id INT,
    nome VARCHAR(100),
    citta VARCHAR(100)
)

Ordini (
    id INT,
    id_cliente INT,
    data_ordine DATE,
    importo DECIMAL(7,2)
)

Le due tabelle sono collegate dalla relazione tra:
Clienti.id e Ordini.id_cliente.

*/

-- ESERCIZIO 1 - INNER JOIN
-- Obiettivo: Visualizza l'elenco dei clienti che hanno effettuato almeno un ordine.
-- Per ciascuno, mostra: nome del cliente, data dell'ordine, importo


-- CREATE DATABASE DBJoin;
-- USE DBJoin;
/*
CREATE TABLE Clienti (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    citta VARCHAR(100)
);
*/

/*
INSERT INTO Clienti (id, nome, citta)
VALUES
(1, 'Lucia', 'Fano'),
(2, 'Marco', 'Roma'),
(3, 'Anna', 'Milano'),
(4, 'Paolo', 'Napoli'),
(5, 'Giulia', 'Bologna'),
(6, 'Andrea', 'Torino'),
(7, 'Sara', 'Firenze'),
(8, 'Luca', 'Genova'),
(9, 'Elena', 'Bari'),
(10, 'Matteo', 'Palermo'),
(11, 'Alessia', 'Ancona'),
(12, 'Davide', 'Pesaro'),
(13, 'Chiara', 'Rimini'),
(14, 'Simone', 'Perugia'),
(15, 'Federica', 'Verona'),
(16, 'Stefano', 'Parma'),
(17, 'Aurora', 'Padova'),
(18, 'Fabio', 'Trieste'),
(19, 'Marta', 'Ravenna'),
(20, 'Roberto', 'Urbino');




CREATE TABLE Ordini (
    id INT PRIMARY KEY,
    id_cliente INT,
    data_ordine DATE,
    importo DECIMAL(7,2)
);



INSERT INTO Ordini (id, id_cliente, data_ordine, importo)
VALUES
(1, 1, '2026-09-01', 120.50),
(2, 1, '2026-09-03', 75.00),
(3, 2, '2026-09-04', 210.90),
(4, 3, '2026-09-05', 45.50),
(5, 3, '2026-09-07', 89.99),
(6, 4, '2026-09-08', 150.00),
(7, 5, '2026-09-09', 34.90),
(8, 5, '2026-09-10', 250.00),
(9, 6, '2026-09-11', 99.90),
(10, 7, '2026-09-12', 65.00),
(11, 8, '2026-09-13', 180.00),
(12, 9, '2026-09-14', 49.90),
(13, 10, '2026-09-15', 300.00),
(14, 2, '2026-09-16', 85.00),
(15, 4, '2026-09-17', 125.50),
(16, 6, '2026-09-18', 70.00),
(17, 8, '2026-09-19', 215.00),

-- Questi tre ordini hanno un id_cliente
-- che non esiste nella tabella Clienti.
-- Serviranno successivamente per la RIGHT JOIN.

(18, 21, '2026-09-20', 55.90),
(19, 22, '2026-09-21', 140.00),
(20, 23, '2026-09-22', 95.00);

*/


-- SELECT * FROM Clienti;
-- SELECT * FROM Ordini;



-- ESERCIZIO 1 - INNER JOIN - 
/*
Obiettivo:
Visualizza l'elenco dei clienti che hanno effettuato
almeno un ordine.

Per ciascuno mostra:
- nome del cliente
- data dell'ordine
- importo
*/

/*
SELECT
    Clienti.nome,
    Ordini.data_ordine,
    Ordini.importo
FROM Clienti
    INNER JOIN Ordini
    ON Clienti.id = Ordini.id_cliente;

*/

-- ESERCIZIO 2 - LEFT JOIN - 
/*
Obiettivo:
Visualizza tutti i clienti, inclusi quelli che non hanno mai effettuato ordini.

Per ciascuno mostra:
- nome del cliente
- data dell'ordine se presente
- importo se presente
*/

/*
SELECT
    Clienti.nome,
    Ordini.data_ordine,
    Ordini.importo
FROM Clienti
    LEFT JOIN Ordini
    ON Clienti.id = Ordini.id_cliente;
*/

-- ESERCIZIO 3 - RIGHT JOIN - 
/*
Obiettivo:
Visualizza tutti gli ordini, anche quelli che non hanno un cliente associato (caso anomalo).

Per ciascuno mostra:
- nome del cliente se esiste
- data ordine
- importo se presente
*/

/*
SELECT
    Clienti.nome,
    Ordini.data_ordine,
    Ordini.importo
FROM Clienti
    RIGHT JOIN Ordini
    ON Clienti.id = Ordini.id_cliente;
*/










