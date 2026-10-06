-- ESERCISIO HAVING , quali continenti hanno almeno 40 paesi

/*
USE world;
SELECT Continent, COUNT(*) AS num_paesi
FROM country
GROUP BY Continent
HAVING num_paesi > 40;

*/

/*
SELECT Continent, 
    ROUND(AVG(LifeExpectancy),1) AS vita_media
FROM country
GROUP BY Continent
HAVING vita_media > 70;
*/

/*
SELECT Continent, COUNT(*) AS paesi_grandi
FROM country
WHERE Population > 1000000
GROUP BY Continent
HAVING paesi_grandi >= 10;

*/

/*
SELECT Region,
       COUNT(*) AS num_paesi
       SUM(Population) AS pop_tot
FROM country
GROUP BY Region
HAVING pop tot > 50000000 AND num_paesi <= 8
ORDER BY pop_tot DESC;
*/

-- Paesi con almeno 3 lingue ufficiali quindi devo fare una join con due tabelle

/*
SELECT co.name AS paese,
        COUNT(*) AS lingue_ufficiali
FROM country co
LEFT JOIN countrylanguage cl ON cl.CountryCode = co.Code
WHERE cl.IsOfficial = 'T'
GROUP BY co.Code, co.Name
HAVING lingue_ufficiali >= 3
ORDER BY lingue_ufficiali DESC, paese;
*/

-- Esercizio 1 (facile): conta e filtra
-- Nella tabella country, mostra i continenti che hanno più di 30 paesi, con il numero di paesi. 
-- Ordina dal più numeroso al meno numeroso.

/*
SELECT Continent, 
        COUNT(*) AS paesi,
        SUM(Population) AS tot_population
FROM country
GROUP BY Continent
HAVING paesi > 30
ORDER BY paesi DESC;
*/

-- Esercizio 2 (facile): somma e filtra
-- Nella tabella city, mostra i codici paese (CountryCode) in cui la somma degli abitanti delle città supera 20 milioni.

/*
SELECT CountryCode,
        SUM(Population) AS tot_popolazione
FROM city
GROUP BY CountryCode
HAVING tot_popolazione >= 20000000
ORDER BY tot_popolazione DESC;
*/

-- Esercizio 3 (sfida): lingue diffuse
-- Nella tabella countrylanguage, mostra le lingue parlate in più di 10 paesi, 
-- con il numero di paesi, ordinate dalla più diffusa.

/*
SELECT
    Language AS lingua,
    COUNT(CountryCode) AS num_paesi  
FROM countrylanguage
GROUP BY lingua
HAVING num_paesi > 10
ORDER BY num_paesi DESC;
*/

-- Esercizio EXISTS
-- Paesi con almeno una citta nella tabella city
/*
SELECT co.Name
FROM country co
WHERE EXISTS (
    SELECT 1
    FROM city ci
    WHERE ci.CountryCode = co.Code
);
*/

-- Paesi che NON hanno città

/*
SELECT co.Name
FROM country co
WHERE NOT EXISTS (
    SELECT 1
    FROM city ci
    WHERE ci.CountryCode = co.Code
);
*/

-- Antarctica se NON ha città

/*
SELECT co.Name
FROM country co
WHERE co.Name = "Antarctica" AND NOT EXISTS (
    SELECT 1
    FROM city ci
    WHERE ci.CountryCode = co.Code
);
*/

-- Paesi che hanno almeno una città con più di 8 milioni di abitanti

/*
SELECT co.Name
FROM country co
WHERE EXISTS (
    SELECT 1
    FROM city ci
    WHERE ci.CountryCode = co.Code
    AND ci.Population > 8000000
)
ORDER BY co.Name;
*/


-- Mostra i paesi in cui sia il tedesco sia l’italiano sono lingue ufficiali.

/* 

SELECT co.Name
FROM country co
WHERE EXISTS (
    SELECT 1
    FROM countrylanguage cl
    WHERE cl.CountryCode = co.Code
    AND cl.Language = 'German'
    AND cl.IsOfficial = 'T'
)
AND EXISTS (
    SELECT 1
    FROM countrylanguage cl
    WHERE cl.CountryCode = co.Code
    AND cl.Language = 'Italian'
    AND cl.IsOfficial = 'T'
);

*/

-- Controllo integrità, paesi con capitale in country che non sono presenti in tabella city

/*
SELECT co.Name, co.Capital AS id_capitale
FROM country co
WHERE co.Capital IS NOT NULL
AND NOT EXISTS (
    SELECT 1
    FROM city ci
    WHERE ci.ID = co.Capital
)
ORDER BY co.Name;


*/
-- Esercizio 1 (facile): almeno una città grande
-- Mostra i paesi che hanno almeno una città con più di 8 milioni di abitanti. 
-- Ordina i nomi in ordine alfabetico.


SELECT co.Name AS Paesi_con_almeno_una_citta_grande
FROM country co
WHERE EXISTS (
    SELECT 1
    FROM city ci
    WHERE ci.CountryCode = co.Code
    AND ci.Population > 8000000
)
ORDER BY co.Name ASC;


-- Esercizio 2 (facile): nessuna città
-- Mostra nome e continente dei paesi che non hanno nessuna città nella tabella city.


SELECT 
    co.Name AS Paesi_senza_citta,
    co.Continent AS Continente
FROM country co
WHERE NOT EXISTS (
    SELECT 1
    FROM city ci
    WHERE ci.CountryCode = co.Code
);


-- Esercizio 3 (sfida): europei senza lingua ufficiale
-- Mostra i paesi europei per cui non è registrata nessuna lingua ufficiale (IsOfficial = 'T') nella tabella countrylanguage.

SELECT COUNT(*) AS Paesi_europei_senza_lingua_ufficiale
FROM country co
WHERE co.Continent = 'Europe' AND
    NOT EXISTS (
    SELECT 1
    FROM countrylanguage cl
    WHERE cl.CountryCode = co.Code AND cl.IsOfficial = 'T'
);



