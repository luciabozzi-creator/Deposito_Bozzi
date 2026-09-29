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

