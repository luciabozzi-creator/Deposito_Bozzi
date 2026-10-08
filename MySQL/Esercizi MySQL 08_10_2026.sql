-- ESERCIZIO TABELLE

/*
-- SELECT COUNT(*) FROM sakila.film_text;

CREATE TABLE lake(
    Name VARCHAR(50), --PRIMARY KEY
    CountryCode                 CHAR(3),
    Surface                     DECIMAL(6, 2),
    Surface                     INT,
    FOREIGN KEY (CountryCode)   REFERENCES country (Code)
);

CREATE TABLE airport(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    Code        CHAR(3) NOT NULL UNIQUE,
    Name        VARCHAR(60) NOT NULL,
    Type        ENUM('International','National', 'Military')
    Status      CHAR(1) NOT NULL DEFAULT 'A'
);

INSERT INTO airport (Code, Name) VALUES ('FCO', 'Leonardo Da Vinci');
-- RIGA: ID=1, Code='FCO', Name='Leonardo Da Vinci', Status='A'

CREATE TABLE monument(
    INDEX           INT AUTO_INCREMENT PRIMARY KEY,
    Name            VARCHAR(60) NOT NULL,
    CityID          INT NOT NULL,
    BuildingYear    INT CHECK(BuildingYear > 0),
    FOREIGN KEY (CityID) REFERENCES City(ID)
);

INSERT TO (Name, CityID, BuildingYear) VALUES ('Torre di Pisa', 345, -145); --

-- La primary key puo essere una coppia di colonne o valori

CREATE TABLE border(
    CodeA CHAR(3) NOT NULL, -- (Composte) Nella coppia di valori A o B si possono ripetere ovviamente in maniera pero univoca a coppia
    CodeB CHAR(3) NOT NULL,
    DistanceKm FLOAT CHECK(DistanceKm > 0),
    PRIMARY KEY (CodeA, CodeB),
    FOREIGN KEY (CodeA) REFERENCES country (Code),
    FOREIGN KEY (CodeB) REFERENCES country (Code),
    CHECK (CodeA <> CodeB) -- Inserisci solo se CodeA è diverso da CodeB
);

INSERT INTO(CodeA, Code B, DistanceKm)
VALUES('ITA','ITA', 100); -- Fallisce perchè i codici sono uguali

INSERT INTO (CodeA, CodeB, DistanceKm)
VALUES('ITA', 'AUT', 0); -- Fallisce perchè la lunghezza è minore di zero

INSERT INTO (CodeA, CodeB, DistanceKm)
VALUES('ITA', 'AUT', 300); -- Funziona

-- AS non copia i vincoli ne le chiavi (primarie e esterne)
CREATE TABLE big_european_cities AS
    SELECT ci.ID, ci.Name AS City, co.Name AS Country, ci.Population
    FROM city ci
    JOIN Country co ON co.code = ci.CountryCode
    WHERE co.Continent = 'Europe'
    AND ci.Population > 1000000;

CREATE TABLE nome_tabella LIKE tabella_originale; -- LIKE copia solo la struttura (vincoli, indici chiavi)

*/

-- Esercizio 1: la prima tabella
-- Crea una tabella fiume con tre colonne: 
-- Nome (testo fino a 50 caratteri), 
-- LunghezzaKm (numero intero), 
-- CountryCode (testo di 3 caratteri).

CREATE TABLE fiume (
    Nome            VARCHAR(50),
    LunghezzaKm     INT,
    CountryCode     CHAR(3)
);

-- Esercizio 2: aggiungi le regole
-- Crea una tabella museo con:
-- ID: intero, chiave primaria, numerazione automatica;
-- Nome: testo fino a 60 caratteri, obbligatorio;
-- Visitatori: intero, con valore predefinito 0.

CREATE TABLE museo (
    ID                  INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(60)    NOT NULL,
    Visitatori          INT DEFAULT 0
);


-- Esercizio 3: collega la tabella a city
-- Crea una tabella ristorante con ID (chiave primaria), 
-- Nome (obbligatorio) e CityID, che deve fare riferimento alla colonna ID della tabella city. 
-- Poi prova a inserire un ristorante a Milano (CityID = 1465) e uno con CityID = 99999. Cosa succede?

CREATE TABLE ristorante (
    ID                      INT PRIMARY KEY,
    Nome                    VARCHAR(60) NOT NULL,
    CityID                  INT,
    FOREIGN KEY (CityID)    REFERENCES city(ID)
);

INSERT INTO ristorante (ID, Nome, CityID)
VALUES (1, 'Ristorante Milano', 1465);

INSERT INTO ristorante (ID, Nome, CityID)
VALUES (2, 'Ristorante Sconosciuto', 99999);

SELECT * FROM ristorante;
SELECT * FROM city WHERE ID = 1465;
SELECT * FROM ristorante WHERE CityID IN ('99999','1465'); -- Verifica che il ristorante con CityID = 99999 non sia stato inserito


-- Esercizio 4: da una query a una tabella
-- Crea una tabella megacitta che contenga 
-- nome, 
-- codice paese e popolazione delle città con più di 5 milioni di abitanti. 
-- Poi conta le righe con una SELECT.

CREATE TABLE megacitta AS
SELECT
    Name,
    CountryCode,
    Population
FROM city
WHERE Population > 5000000;

SELECT COUNT(*) FROM megacitta; -- Conta le righe della nuova tabella

/* -- ESERCIZI ALTER TABLE

CREATE TABLE lake(
    Name            VARCHAR(50), --PRIMARY KEY
    CountryCode     CHAR(3),
    Surface         DECIMAL(6, 2),
    FOREIGN KEY (CountryCode) REFERENCES country (Code)
);

ALTER TABLE lake
ADD COLUMN Profondita DECIMAL(6,2);

ALTER TABLE lake
MODIFY COLUMN Name VARCHAR(50) NOT NULL;

INSERT INTO lake(CountryCode, Surface, Profondita)
VALUES ('AAA', 100, 100)

ALTER TABLE lake
RENAME COLUMN Surface TO SurfaceKm;

ALTER TABLE lake
DROP COLUMN Profondita;


ALTER TABLE lake
ADD CONSTRAINT CountryCode
FOREIGN KEY (CountryCode) REFERENCES country (Code),
ADD CONSTRAINT CountryCode
UNIQUE;

CREATE TABLE city_copia AS SELECT * FROM city;

ALTER TABLE city_copia
ADD COLUMN Milionaria CHAR(1) NOT NULL DEFAULT 'N',
ADD INDEX idx_paese (CountryCode);

UPDATE city_copia
SET Milionaria = 'S'
WHERE Population >= 1000000;

ALTER TABLE city_copia TO citta_copia;

*/
-- Esercizio 1: aggiungi una colonna
-- Aggiungi alla tabella sede una colonna Telefono di tipo testo, fino a 20 caratteri.

CREATE TABLE sede (
ID INT PRIMARY KEY,
Nome VARCHAR(20),
CityID INT
);

ALTER TABLE sede
ADD COLUMN Telefono VARCHAR(20);

SELECT * FROM sede;

-- Esercizio 2: cambia una colonna
-- Il nome delle sedi è troppo corto. Portalo a 60 caratteri e rendilo obbligatorio.

ALTER TABLE sede
MODIFY COLUMN Nome VARCHAR(60) NOT NULL;

-- Esercizio 4: collega le sedi alle città
-- Aggiungi a sede una chiave esterna che colleghi CityID alla colonna ID di city. 
-- Poi inserisci una sede a Roma (CityID = 1464) e una con CityID = 99999. Cosa succede?

ALTER TABLE sede
ADD CONSTRAINT fk_sede_city
FOREIGN KEY (CityID) REFERENCES city(ID);

INSERT INTO sede (ID, Nome, CityID)
VALUES (1, 'Sede Roma', 1464);

INSERT INTO sede (ID, Nome, CityID)
VALUES (2, 'Sede Test', 99999);

SELECT * FROM sede;
