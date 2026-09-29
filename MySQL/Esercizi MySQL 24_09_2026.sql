-- ESERCIZI DELLA GIORNATA 24_09_2026

-- 27) Esercizio recap di Where e condizioni

-- SELECT * FROM world.countrylanguage WHERE IsOfficial = 'F'; -- Elenco lingue non ufficiali
-- SELECT * FROM world.countrylanguage WHERE IsOfficial <> 'F'; -- Elenco lingue che non sono non ufficiali
-- SELECT * FROM world.countrylanguage WHERE Percentage >= 90 AND IsOfficial = 'T'; -- Elenco lingue ufficiali con percentuale superiore uguale 90%
-- SELECT * FROM world.countrylanguage WHERE Percentage BETWEEN 50 AND 89.9 AND IsOfficial = 'T'; -- Elenco lingue ufficiali con percentuale fra 50 e 89.9
-- SELECT * FROM world.countrylanguage WHERE Percentage BETWEEN 0 AND 49.9 AND IsOfficial = 'T'; -- Elenco lingue ufficiali con percentuale fra 0 e 49.9

-- Elenco lingue ufficiali o che non terminano per "H" con percentuale uso fra 0 e 50 escluso
-- SELECT * FROM world.countrylanguage WHERE Percentage BETWEEN 0 AND 49.9 AND (IsOfficial = 'T' OR NOT Language LIKE '%h');

-- Ora lo ordino per percentuale crescente

/* SELECT * FROM world.countrylanguage 
    WHERE Percentage BETWEEN 0 AND 49.9 AND (IsOfficial = 'T' OR NOT Language LIKE '%h')
    ORDER BY Percentage ASC;
*/

-- Esercizio con null e not null

/* 
SELECT * FROM world.country
WHERE IndepYear IS NOT NULL AND LifeExpectancy IS NULL; -- Annno di indipendenza non è vuoto e aspettativa di vita vuoto
*/

-- Esercizio con GROUP BY

/*
SELECT CountryCode, COUNT(*) AS NumeroCitta
    FROM world.city
    GROUP BY CountryCode;
*/

/*  ESERCIZI SLIDE TESTO LIBERO


ESERCIZIO 1: utilizzo di DISTINCT e WHERE

Elencare senza ripetizioni -----> DISTINCT
tutte le regioni (Region)
dei paesi che appartengono al continente (Continent) 'Europe' ---> Condizione WHERE 

/*

SELECT DISTINCT Region, Continent 
FROM world.country
WHERE Continent = 'Europe';

*/

/* ESERCIZIO 2: combinazione di WHERE, ORDER BY

Elencare i nomi (Name) e popolazione (Population) ----> Selezione
delle città (City) --> Tabella
degli stati uniti (Country Code USA) --- Condizione 1 --- E ---
che hanno una popolazione superiore a 1 milione di abitanti --- Condizione 2 --- operatore maggiore uguale
ordinando i risultati dalla città piu popolosa alla meno popolosa ---- Ordinamento */

/*

SELECT Name, Population
FROM world.city
WHERE CountryCode ='USA' AND Population >= 1000000
ORDER BY Population DESC;

*/

/* ESERCIZIO 3: GROUP BY con funzioni di aggregazione

Mostrare per ogni continente ---> Selezione Distinct --- Continent
presente nella tabella country ---> Tabella country
il numero totale di paesi (Name) appartenenti a ciascun continente ---> condizione 1 ---- E----
la popolazione totale del continente ---> condizione 2
ordinare il risultato per popolazione totale in ordine descrescente

*/

/*

SELECT Continent, 
    COUNT(Name) AS NumberOfCountries, 
    SUM(Population) AS ContinentPopulation
FROM world.country
GROUP BY Continent
ORDER BY ContinentPopulation DESC;

/*

/*
SELECT Name, COUNT(Name) AS Total --- Test per vedere se ho duplicati su Name 1 o 2
FROM world.country
GROUP BY Name
ORDER By Name DESC;

*/ 

/* ESERCIZIO 4: Combinazione di WHERE, GROUP BY e ORDER BY

Mostrare, per ogni CountryCode, ----> selezione gruppo, codice paese country code, numero di città trovate conteggio, popolazionetotale città totale somma
il numero di città presenti ---> conteggio count
nella tabella city ---> tabella
che hanno una popolazione maggiore di 500 mila abitanti ---> condizione where
ordinare i paesi dal maggior numero citta al minor numero ---> ordinamento

*/

-- SELECT CountryCode FROM world.city;

SELECT CountryCode AS Codice_Paese,
    COUNT(Name) AS Numero_Citta, 
    SUM(Population) AS Popolazione_Totale
FROM world.city
WHERE Population >= 500000
GROUP BY Codice_Paese
ORDER BY Popolazione_Totale DESC;
