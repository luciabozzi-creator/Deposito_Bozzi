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


SELECT * FROM DBVendite.Clienti

-- DROP TABLE world.Clienti

-- 1. Clienti con email su dominio Gmail


-- 2. Seleziona tutti i clienti la cui email termina con @gmail.com


-- 3. Clienti con nome che inizia con la lettera 'A'


-- 4. Mostra tutti i clienti il cui nome comincia con la lettera A


-- 5. Clienti con cognome che contiene esattamente 5 lettere


-- 6. Mostra tutti i clienti il cui cognome è composto da esattamente 5 caratteri


-- 7. Clienti con età compresa tra 30 e 40 anni (inclusi)


-- 8. Elenca i clienti che hanno un'età compresa tra 30 e 40 anni, inclusi gli estremi


-- 9. Clienti che vivono in città il cui nome contiene "roma"
--    ignorando maiuscole/minuscole


-- 10. Mostra tutti i clienti che abitano in una città il cui nome
--     contiene la stringa "roma", indipendentemente da maiuscole o minuscole