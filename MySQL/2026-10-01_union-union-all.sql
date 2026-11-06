-- ESERCIZIO UNION E UNION ALL, 
-- le join lavorano sul dato in orrizzontale mentre le union in verticale cioe aggiungono sopra e sotto
-- UNION ALL TUTTO MENTRE UNION ELIMINA I RIPETUTI
/*
USE world;
SELECT 'Europe' as continente
UNION 
SELECT 'Europe' as continente;
*/

/*
SELECT
    Name,
    'Capitale' AS Categoria
FROM city
WHERE ID IN (Select Capital FROM Country)

UNION

SELECT
    Name,
    'Metropoli' AS Categoria
FROM city
WHERE Population > 3000000;
*/

-- ESERCIZIO HAVING 
/*
SELECT 
    Continent,
    COUNT(*) AS TotaleNazioni
FROM country
GROUP BY Continent

HAVING count(*) > 30;
*/

/*
SELECT 
    Continent,
    ROUND(AVG(LifeExpectancy),1) AS MediaAspettativa

FROM country
WHERE Population > 1000000
GROUP BY Continent

HAVING AVG(LifeExpectancy) > 70;
*/

-- ESERCIZIO CON EXISTS
/*
SELECT
    co.name
FROM country co
WHERE EXISTS (
      SELECT 1
      FROM city ci
      WHERE ci.CountryCode = co.code
)
LIMIT 5;
*/

-- ESERCIZIO CON ANY - in base alla popolazione della citta piu piccola italiana, almeno una vera
/*
SELECT
    Name,
    Population
FROM city
WHERE Population > any (
      SELECT Population
      FROM city
      WHERE CountryCode = 'NLD'
);
*/

-- ESERCIZIO ALL - in base città piu grande italiana, tutte le condizioni
SELECT
    Name,
    Population
FROM city
WHERE Population > ALL (
       SELECT Population
       FROM city
       WHERE CountryCode ='ITA'
)
ORDER BY Population ASC
LIMIT 20;