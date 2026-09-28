-- Conteggio città con popolazione fra 5 mila e 1 milione
/* 
SELECT CountryCode AS Codice_Nazione,
    COUNT(Name) AS Numero_Citta, 
    SUM(Population) AS Popolazione_Totale
FROM world.city
WHERE Population BETWEEN 500000 AND 1000000
GROUP BY Codice_Nazione
ORDER BY Popolazione_Totale ASC;
*/

-- Lista città italiane per popolazione fra 500 mila e 1 milione
/* 
SELECT *
FROM world.city
WHERE Population BETWEEN 500000 AND 1000000 AND CountryCode = 'ITA'
ORDER BY Population ASC;
*/

/*
SELECT COUNT(*)
FROM world.city
WHERE Population BETWEEN 500000 AND 1000000
AND CountryCode = 'ITA'
ORDER BY Population ASC;
*/
/* 
SELECT Continent, GovernmentForm,
    COUNT(*) AS NumberOfCountries 
FROM world.country
WHERE Continent IN ('Asia','North America','South America')
GROUP BY Continent, GovernmentForm;
*/
/*
SELECT Continent, 
    COUNT(Name) AS NumberOfCountries, 
    SUM(Population) AS ContinentPopulation
FROM world.country
GROUP BY Continent
ORDER BY ContinentPopulation DESC;
*/
