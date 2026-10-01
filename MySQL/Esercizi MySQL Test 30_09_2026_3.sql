/*
ESERCIZIO - REPORT REPARTO VENDITE
Devi realizzare un report completo per il reparto vendite,
che soddisfi tutte le seguenti condizioni usando correttamente
e separatamente i tre tipi di JOIN:


1. CLIENTI ATTIVI
Elenca i clienti attivi, cioè quelli che hanno effettuato
almeno un ordine, mostrando per ciascuno:
- Nome del cliente
- Totale ordini effettuati
- Somma totale degli importi spesi


2. CLIENTI INATTIVI
Elenca i clienti inattivi, cioè quelli che non hanno
mai effettuato ordini, mostrando solo:
- Nome del cliente
- Città di residenza


3. ORDINI ORFANI
Individua gli ordini orfani, cioè ordini presenti in tabella
ma senza un cliente valido associato
(es. cliente cancellato), e mostra:
- ID dell'ordine
- Data dell'ordine
- Importo
- Cliente = NULL

REQUISITI TECNICI:
- Per il punto 1: usa INNER JOIN.
- Per il punto 2: usa LEFT JOIN con condizione su IS NULL.
- Per il punto 3: usa RIGHT JOIN con condizione su IS NULL.
*/

-- CREAZIONE DATABASE

-- CREATE DATABASE DBReportVendite;
USE DBReportVendite;

-- CREAZIONE TABELLA CLIENTI
/*
CREATE TABLE Clienti (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    citta VARCHAR(100)
);

-- INSERIMENTO CLIENTI

INSERT INTO Clienti (id, nome, citta)
VALUES
(1, 'Laura', 'Roma'),
(2, 'Matteo', 'Milano'),
(3, 'Giulia', 'Fano'),
(4, 'Andrea', 'Bologna'),
(5, 'Sara', 'Firenze'),
(6, 'Luca', 'Torino'),
(7, 'Elena', 'Ancona'),
(8, 'Marco', 'Napoli'),
(9, 'Chiara', 'Pesaro'),
(10, 'Davide', 'Rimini'),
(11, 'Alessia', 'Perugia'),
(12, 'Paolo', 'Verona'),
(13, 'Federica', 'Parma'),
(14, 'Simone', 'Genova'),
(15, 'Aurora', 'Padova'),
(16, 'Fabio', 'Bari'),
(17, 'Marta', 'Urbino'),
(18, 'Stefano', 'Ravenna'),
(19, 'Anna', 'Palermo'),
(20, 'Roberto', 'Trieste');

-- CREAZIONE TABELLA ORDINI

CREATE TABLE Ordini (
    id INT PRIMARY KEY,
    id_cliente INT,
    data_ordine DATE,
    importo DECIMAL(7,2)
);


-- INSERIMENTO ORDINI

INSERT INTO Ordini (id, id_cliente, data_ordine, importo)
VALUES
(1, 1, '2026-09-01', 120.50),
(2, 1, '2026-09-05', 75.00),
(3, 1, '2026-09-12', 210.00),

(4, 2, '2026-09-02', 89.90),
(5, 2, '2026-09-18', 150.00),

(6, 3, '2026-09-03', 45.50),
(7, 3, '2026-09-20', 130.00),

(8, 4, '2026-09-04', 250.00),

(9, 5, '2026-09-06', 35.90),
(10, 5, '2026-09-22', 99.90),

(11, 6, '2026-09-07', 180.00),
(12, 7, '2026-09-08', 49.90),
(13, 8, '2026-09-09', 300.00),
(14, 9, '2026-09-10', 85.00),
(15, 10, '2026-09-11', 125.50),

-- ORDINI ORFANI:
-- gli id_cliente 21, 22 e 23 non esistono in Clienti

(16, 21, '2026-09-23', 55.90),
(17, 22, '2026-09-24', 140.00),
(18, 23, '2026-09-25', 95.00),

(19, 4, '2026-09-26', 70.00),
(20, 6, '2026-09-27', 215.00);

*/


-- SELECT * FROM Clienti;
-- SELECT * FROM Ordini;

-- ESERCIZIO: REPORT REPARTO VENDITE

-- Devi realizzare un report completo per il reparto vendite,
-- che soddisfi tutte le seguenti condizioni usando correttamente
-- e separatamente i tre tipi di JOIN.


-- PUNTO 1 - CLIENTI ATTIVI

-- Elenca i clienti attivi, cioè quelli che hanno effettuato
-- almeno un ordine, mostrando per ciascuno:

-- Nome del cliente
-- Totale ordini effettuati
-- Somma totale degli importi spesi

-- Requisito tecnico:
-- usare INNER JOIN.

/*
SELECT 
    Clienti.nome,
    SUM(Ordini.importo) AS Totale_Importi_Spesi,
    COUNT(Ordini.id) AS Numero_ordini_per_ciascun_cliente
FROM Clienti
INNER JOIN Ordini
    ON Clienti.id = Ordini.id_cliente
 GROUP BY Clienti.nome;
*/


-- PUNTO 2 - CLIENTI INATTIVI

-- Elenca i clienti inattivi, cioè quelli che non hanno
-- mai effettuato ordini, mostrando solo:

-- Nome del cliente
-- Città di residenza

-- Requisito tecnico:
-- usare LEFT JOIN con condizione su IS NULL.
/*
SELECT 
    Clienti.nome,
    Clienti.citta,
    Ordini.importo
FROM Clienti
LEFT JOIN Ordini
    ON Clienti.id = Ordini.id_cliente
WHERE Ordini.importo IS NULL;
*/

-- PUNTO 3 - ORDINI ORFANI

-- Individua gli ordini orfani, cioè ordini presenti in tabella
-- ma senza un cliente valido associato
-- (es. cliente cancellato), e mostra:

-- ID dell'ordine
-- Data dell'ordine
-- Importo
-- Cliente = NULL

-- Requisito tecnico:
-- usare RIGHT JOIN con condizione su IS NULL.

SELECT 
    Clienti.nome,
    Ordini.id,
    Ordini.data_ordine,
    Ordini.importo
FROM Clienti
RIGHT JOIN Ordini
    ON Clienti.id = Ordini.id_cliente
WHERE Clienti.nome IS NULL;
