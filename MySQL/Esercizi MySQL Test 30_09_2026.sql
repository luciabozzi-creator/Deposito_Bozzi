-- ESEMPIO INNER JOIN

/*
USE world;
SELECT 
    ci.name AS Citta,
    co.name AS Nazione,
    co.Continent
FROM city ci -- qui la tabella city la rinomino CI
INNER JOIN country co -- INNER JOIN CIOE SOLO I RECORD IN COMUNE, qui la tabella country la rinomino CO
    ON ci.CountryCode = co.Code -- Chiave in comune
WHERE ci.CountryCode = 'ITA'
LIMIT 5;
*/

-- ESEMPIO SOLO LINGUE UFFICIALI ASSOCIATE ALLO STATO EUROPEO
/*
USE world;
SELECT
    country.Name AS Nazione,
    countrylanguage.Language,
    countrylanguage.Percentage
FROM country
INNER JOIN countrylanguage
    on country.code = countrylanguage.CountryCode
WHERE countrylanguage.IsOfficial = 'T'
    AND country.Continent = 'Europe';
*/

-- ESEMPIO VOGLIO IL NOME DELLO STATO E LA SUA CAPITALE XXX DA CORREGGERE
/*
USE world;
SELECT
    country.Name as Nazione,
    city.Name AS NomeCitta
FROM country
INNER J0IN city
    ON country.capital = city.id
WHERE country.Continent = 'Europe'
LIMIT 10;
*/

-- ESEMPIO VOGLIO LE NAZIONI CHE NON HANNO REGISTRATO NESSUNA CITTA LEFT JOIN
/*
USE world;
SELECT
    country.Name AS Nazione,
    city.Name AS NomeCitta
FROM country
LEFT JOIN city
    on Country.Code = city.CountryCode
WHERE city.name IS NULL;
*/

-- ESEMPIO VOGLIO LE NAZIONI CHE NON HANNO REGISTRATO NESSUNA CITTA LEFT JOIN
/*
CREATE TEMPORARY TABLE clienti (
    id INT,
    nome VARCHAR(50)
);

CREATE TEMPORARY TABLE acquisti (
    id INT,
    id_cliente INT,
    totale DECIMAL(5,2)
);

INSERT INTO clienti VALUES
    (1, 'Mario Rossi'),
    (2, 'Giovanni Storti');

INSERT INTO acquisti VALUES
    (101,1,49.99);
*/
/*
-- SELECT totale FROM acquisti, questa non va;
SELECT
    clienti.nome,
    acquisti.totale
    FROM clienti
    LEFT JOIN acquisti
    ON clienti.id = acquisti.id;


-- SELECT totale FROM acquisti, questa non va;
SELECT
    acquisti.id AS ID_Ordine,
    acquisti.totale,
    clienti.nome

FROM clienti
RIGHT JOIN acquisti
    ON clienti.id = acquisti.id_cliente
    WHERE clienti.id IS NULL;

*/
/*
-- ESEMPIO CROSS JOIN
CREATE TEMPORARY TABLE colori (
    colore VARCHAR(20)
);

CREATE TEMPORARY TABLE taglie (
    taglia VARCHAR(10)
);

INSERT INTO colori VALUES
('Rosso'),
('Blu');
INSERT INTO taglie VALUES
('S'),
('M'),
('L');

SELECT
    colori.colore,
    taglie.taglia
FROM colori
CROSS JOIN taglie;

*/





