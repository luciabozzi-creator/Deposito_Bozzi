/* 
Si consideri una tabella chiamata Vendite con la seguente struttura, almeno 20 elementi generati:
Vendite (
    id INT,
    prodotto VARCHAR(100),
    categoria VARCHAR(50),
    quantita INT,
    prezzo_unitario DECIMAL(6,2),
    data_vendita DATE
)

Scrivi le query SQL per rispondere alle seguenti richieste:
- Totale vendite per categoria
- Visualizza, per ogni categoria, il numero totale di vendite effettuate.
- Prezzo medio per categoria
- Mostra, per ogni categoria, il prezzo medio dei prodotti venduti.
- Quantità totale venduta per ogni prodotto
- Mostra il totale delle quantità vendute (SUM) per ciascun prodotto.
- Prezzo massimo e minimo venduto nella tabella
- Mostra il prezzo massimo e il prezzo minimo tra tutti i prodotti venduti.
- Numero totale di righe nella tabella
- Conta quante vendite sono state registrate nella tabella Vendite.
- I 5 prodotti più costosi (in base al prezzo_unitario)
- Elenca i 5 prodotti più costosi ordinati in modo decrescente rispetto al prezzo.
- I 3 prodotti meno venduti per quantità totale
- Mostra i nomi dei 3 prodotti con la quantità totale più bassa venduta (usa SUM e LIMIT).
 */

 -- CREATE DATABASE DBVendite;
 
/*
CREATE TABLE DBVendite.Vendite (
    id INT,
    prodotto VARCHAR(100),
    categoria VARCHAR(50),
    quantita INT,
    prezzo_unitario DECIMAL(6,2),
    data_vendita DATE
);
*/

/*
INSERT INTO DBVendite.Vendite (id, prodotto, categoria, quantita, prezzo_unitario, data_vendita)
VALUES
(1,'Mouse Wireless','Elettronica',3,24.90,'2026-09-01'),
(2,'Tastiera','Elettronica',2,49.90,'2026-09-02'),
(3,'Mouse Wireless','Elettronica',5,24.90,'2026-09-03'),
(4,'Monitor','Elettronica',1,249.99,'2026-09-04'),
(5,'Tastiera','Elettronica',4,45.90,'2026-09-05'),
(6,'Lampada','Casa',2,35.50,'2026-09-06'),
(7,'Sedia','Casa',1,129.90,'2026-09-07'),
(8,'Lampada','Casa',6,32.50,'2026-09-08'),
(9,'Tavolo','Casa',1,399.00,'2026-09-09'),
(10,'Sedia','Casa',3,119.90,'2026-09-10'),
(11,'Caffè','Alimentari',10,4.50,'2026-09-11'),
(12,'Pasta','Alimentari',20,1.20,'2026-09-12'),
(13,'Caffè','Alimentari',8,4.80,'2026-09-13'),
(14,'Olio','Alimentari',4,12.90,'2026-09-14'),
(15,'Pasta','Alimentari',15,1.10,'2026-09-15'),
(16,'Penna','Cancelleria',30,0.80,'2026-09-16'),
(17,'Quaderno','Cancelleria',12,3.50,'2026-09-17'),
(18,'Penna','Cancelleria',25,0.75,'2026-09-18'),
(19,'Evidenziatore','Cancelleria',2,2.20,'2026-09-19'),
(20,'Quaderno','Cancelleria',9,3.80,'2026-09-20');
*/

-- DROP TABLE DBVendite.Vendite;
-- DELETE FROM DBVendite.Vendite;

SELECT * FROM DBVendite.Vendite;

-- TOTALE VENDITE PER CATEGORIA
SELECT categoria, COUNT(*) AS Totale_Vendite_Categoria
FROM DBVendite.Vendite
GROUP BY categoria;

-- VISUALIZZA PER OGNI CATEGORIA IL PREZZO MEDIO PER CATEGORIA
SELECT categoria, ROUND(AVG(prezzo_unitario),2) AS Prezzo_Medio_Categoria
FROM DBVendite.Vendite
GROUP BY categoria;

-- TOTALE QUANTITA PER PRODOTTO
SELECT prodotto, SUM(Quantita) AS Quantita_Vendite_Prodotto
FROM DBVendite.Vendite
GROUP BY prodotto;

-- PREZZO MASSIMO E MINIMO VENDUTO NELLA TABELLA
SELECT 
    MAX(prezzo_unitario) AS Prezzo_Massimo,
    MIN(prezzo_unitario) AS Prezzo_Minimo
FROM DBVendite.Vendite;

-- NUMERO TOTALE DI RIGHE NELLA TABELLA
SELECT COUNT(*) AS Numero_Righe
FROM DBVendite.Vendite;

-- I CINQUE PRODOTTI PIU COSTOSI ORDINATI IN MODO DECRESCENTE RISPETTO AL PREZZO
SELECT DISTINCT prodotto, prezzo_unitario
FROM DBVendite.Vendite
ORDER BY prezzo_unitario DESC
LIMIT 5; 

-- I 3 PRODOTTI MENO VENDUTI PER QUANTITA TOTALE
SELECT 
    prodotto, 
    SUM(quantita) AS PezziVenduti
FROM DBVendite.Vendite
GROUP BY prodotto
ORDER BY PezziVenduti DESC
LIMIT 3;

