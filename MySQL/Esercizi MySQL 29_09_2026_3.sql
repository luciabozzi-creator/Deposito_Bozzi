-- ESERCIZIO TABELLA CLIENTI

-- Creazione della tabella Clienti
/*
CREATE TABLE DBVendite.Clienti (
    id INT,
    nome VARCHAR(100),
    cognome VARCHAR(100),
    email VARCHAR(100),
    eta INT,
    citta VARCHAR(100)
);

*/

-- Inserimento di almeno 20 clienti
INSERT INTO DBVendite.Clienti (id, nome, cognome, email, eta, citta)
VALUES
(1,'Anna','Rossi','anna.rossi@gmail.com',32,'Roma'),
(2,'Marco','Verdi','marco.verdi@yahoo.it',45,'Milano'),
(3,'Alice','Bianchi','alice.bianchi@gmail.com',28,'Roma'),
(4,'Luca','Neri','luca.neri@hotmail.com',35,'Torino'),
(5,'Andrea','Costa','andrea.costa@gmail.com',40,'Bologna'),
(6,'Paolo','Ricci','paolo.ricci@yahoo.it',38,'Firenze'),
(7,'Alessia','Greco','alessia.greco@gmail.com',31,'Roma'),
(8,'Matteo','Bruni','matteo.bruni@hotmail.com',25,'Napoli'),
(9,'Giulia','Gallo','giulia.gallo@gmail.com',39,'Palermo'),
(10,'Antonio','Conti','antonio.conti@yahoo.it',42,'Genova'),
(11,'Arianna','Leone','arianna.leone@gmail.com',30,'Roma'),
(12,'Davide','Marini','davide.marini@hotmail.com',36,'Bari'),
(13,'Alberto','Rizzo','alberto.rizzo@gmail.com',41,'Verona'),
(14,'Simone','Lombardi','simone.lombardi@yahoo.it',29,'Parma'),
(15,'Amelia','Serra','amelia.serra@gmail.com',34,'Roma'),
(16,'Fabio','Villa','fabio.villa@hotmail.com',37,'Padova'),
(17,'Aurora','Ferri','aurora.ferri@gmail.com',33,'Roma'),
(18,'Stefano','Moretti','stefano.moretti@yahoo.it',46,'Trieste'),
(19,'Angela','Testa','angela.testa@gmail.com',40,'Roma'),
(20,'Roberto','Fiore','roberto.fiore@hotmail.com',27,'Ravenna');


-- SELECT * FROM DBVendite.Clienti

-- DROP TABLE world.Clienti

-- LISTA CLIENTI CON EMAIL CON DOMINIO GMAIL

SELECT nome, cognome, email
FROM DBVendite.Clienti
WHERE email LIKE '%@gmail.com';


-- CLIENTI CON IL NOME CHE INIZIA PER A

SELECT nome, cognome, email
FROM DBVendite.Clienti
WHERE nome LIKE 'A%';


-- CLIENTI CON COGNOME COMPOSTO DI 5 CARATTERI

SELECT cognome
FROM DBVendite.Clienti
WHERE cognome LIKE '_____';


-- CLIENTI CON ETA FRA I 30 E 40

SELECT *
FROM DBVendite.Clienti
WHERE eta BETWEEN 30 AND 40;


-- TUTTI I CLIENTI CHE VIVONO IN UNA CITTA CHE CONTIENE ROMA

SELECT *
FROM Clienti
WHERE citta LIKE '%roma%';