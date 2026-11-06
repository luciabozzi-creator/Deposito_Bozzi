-- ESERCIZI SUL JOIN DI TABELLE
-- 1. INNER JOIN – Mostra il nome di ogni città accanto al nome del suo paese (bastano le prime 20 righe).

SELECT 
    city.Name AS Citta, 
    country.Name AS Paese
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code
LIMIT 20;

-- 2. INNER JOIN + WHERE – Mostra tutte le città italiane con la loro popolazione, usando il nome del paese ('Italy') e non il codice.

SELECT 
    city.Name AS Citta, 
    city.Population AS Popolazione
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code
WHERE country.Name = 'Italy';

-- 3. INNER JOIN + ORDER BY – Mostra le 10 città più popolose del mondo con il nome del paese.

SELECT 
    country.Name AS Paese,
    city.Name AS Citta, 
    city.Population AS Popolazione
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code
ORDER BY city.Population DESC
LIMIT 10;

-- 4. INNER JOIN su un'altra colonna – Mostra ogni paese europeo con il nome della sua capitale.

SELECT country.Name AS Paese,
       city.Name AS Capitale
FROM country
INNER JOIN city
ON country.Capital = city.ID
WHERE country.Continent = 'Europe';

-- 5. INNER JOIN con countrylanguage – Mostra tutte le lingue parlate in Spagna con la percentuale di parlanti.

SELECT countrylanguage.Language AS Lingua,
       countrylanguage.Percentage AS Percentuale
FROM country
INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
WHERE country.Name = 'Spain';

-- 6. LEFT JOIN – Mostra tutti i paesi con il numero delle loro città, inclusi quelli che ne hanno zero.

SELECT country.Name AS Paese,
       COUNT(city.ID) AS Numero_Citta
FROM country
LEFT JOIN city
    ON country.Code = city.CountryCode
GROUP BY country.Name;

-- 7. LEFT JOIN + IS NULL – Mostra solo i paesi che non hanno nessuna città registrata.

SELECT country.Name AS Paese
FROM country
LEFT JOIN city
    ON country.Code = city.CountryCode
WHERE city.ID IS NULL;

-- 8. JOIN a tre tabelle – Mostra le città con più di 5.000.000 di abitanti, 
-- il nome del loro paese e le lingue ufficiali di quel paese.

SELECT city.Name AS Citta,
       city.Population AS Popolazione,
       country.Name AS Paese,
       countrylanguage.Language AS Lingua_Ufficiale
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code
INNER JOIN countrylanguage
    ON country.Code = countrylanguage.CountryCode
WHERE city.Population > 5000000
AND countrylanguage.IsOfficial = 'T';

