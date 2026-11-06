-- ESERCIZIO SELECT TOP, LIMITA I RISULTATI A UN DETERMINATO NUMERO DI RECORD, ALIAS
USE world;

SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 3;

SELECT Name, SurfaceArea
FROM country
ORDER BY SurfaceArea ASC
LIMIT 6;

SELECT
    Name AS NomeCittà,
    District AS Regione,
    Population AS Residenti
FROM world.city
WHERE Countrycode ='ITA'
LIMIT 5;


-- ESERCIZIO MINIMO E MASSIMO

SELECT
    MIN(Population) AS Cittapiupiccola,
    MAX(Population) AS Cittapiugrande
FROM world.city
WHERE Countrycode = 'ITA';

SELECT
    MIN(SurfaceArea) AS menoKM,
    MAX(SurfaceArea) AS PiuKM
FROM world.country
WHERE Continent = 'Europe';

-- ESERCIZIO SOMMA MEDIA CONTEGGIO

SELECT
    COUNT(*) AS TotaleCitta,
    SUM(Population) AS TotaleAbitanti,
    ROUND(AVG(Population),2) AS Mediaabitanti
FROM world.city
WHERE CountryCode = 'ITA';

SELECT
    SUM(Population) AS TotaleAbitantimondo
FROM country;

-- ESERCIZIO SQL WILDCARD CHARACTERS, LIKE, %, __
SELECT
    name 
FROM world.city
WHERE Countrycode = 'USA'
    AND name LIKE 'a%' or '%an'; -- Inizia con A o finisce come AN

-- ESERCIZIO SQL IN
SELECT
    name,
    continent,
    population
FROM world.country
WHERE code IN ('ITA', 'FRA','DEU');

SELECT
    name,
    CountryCode
FROM world.city
WHERE CountryCode IN ('ITA', 'FRA','ITA')
LIMIT 6;

-- ESERCIZIO SQL NOT

SELECT
    Name,
    CountryCode
FROM world.city
WHERE CountryCode NOT IN ('ITA', 'FRA','ITA')
LIMIT 6;

-- ESERCIZIO BETWEEN NUMERICO

SELECT
    Name,
    Population
FROM world.city
WHERE CountryCode = 'ITA'
    AND population BETWEEN 200000 AND 500000
ORDER BY Population DESC;

-- ESERCIZIO BETWEEN DATE

SELECT
    Name,
    IndepYear
FROM world.country
WHERE IndepYear BETWEEN 1900 AND 1950
ORDER BY IndepYear ASC;

-- ESERCIZIO BETWEEN DATE

SELECT
    Name,
    IndepYear
FROM world.country
WHERE IndepYear BETWEEN 1900 AND 1950
ORDER BY IndepYear ASC;


USE world;

CREATE TEMPORARY TABLE demo_ordini (
    id INT,
    OrderDate DATE
);

INSERT INTO demo_ordini VALUES
(1, '1996-07-04'),
(2, '1996-07-15'),
(3, '1996-08-01');

SELECT *
FROM demo_ordini
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';


