-- Esercizi DEL 28_09_2026: CREATE TABLE, INSERT INTO, UPDATE, DROP TABLE, DELETE

/*
CREATE TEMPORARY TABLE ProvaTabellaNuova ( 
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50), 
voto INT 
);
 

INSERT INTO world.ProvaTabellaNuova (nome,voto) -- inserisco record
VALUES ('Elena Verdi',28),
       ('Paolo Rossi',29);

UPDATE world.ProvaTabellaNuova -- aggiorno record dove nome è Maria Viola
SET nome = 'Maria Viola'
WHERE nome = 'Elena Verdi';


UPDATE world.ProvaTabellaNuova -- aggiorno il record due con nome e voto predefiniti
SET nome = 'Giulia de Bianchi', 
    voto = 30
WHERE id = 2;

-- Ora voglio assegnare un voto in piu a chi ha meno di 30

UPDATE world.ProvaTabellaNuova
SET voto = voto + 1
WHERE voto < 30;

*/


-- DROP TABLE ProvaTabellaNuova -- Ora voglio eliminare la tabella

-- Elimino un record utilizzando l'id
/*
DELETE FROM ProvaTabellaNuova
WHERE id = 1; -- NB: la chiave primaria generata automaticamente non si corregge da sola

SELECT * FROM world.ProvaTabellaNuova
*/

-- Svuoto la tabella

DELETE FROM ProvaTabellaNuova
WHERE id > 0;

SELECT COUNT(*) AS Righe FROM world.ProvaTabellaNuova -- Conto le righe e noto che si è svuotata la tabella




/*
Esercizio sui comandi SQL: GROUP BY, ORDER BY e INSERT INTO
Si consideri un database che contiene informazioni su una libreria. Nel database è presente una tabella chiamata Libri con la seguente struttura:
Libri (
    id INT PRIMARY KEY,
    titolo VARCHAR(100),
    autore VARCHAR(100),
    genere VARCHAR(50),
    prezzo DECIMAL(5,2),
    anno_pubblicazione INT
)
1) Inserimento dati (INSERT INTO)
Inserire almeno 6 nuovi libri nella tabella Libri usando il comando SQL INSERT INTO.
 I libri devono appartenere a generi e autori diversi, ed essere pubblicati in anni differenti.
2) Aggregazione e raggruppamento (GROUP BY)
Scrivere una query che, usando il comando GROUP BY, mostri per ogni genere:
il numero totale di libri presenti;
il prezzo medio dei libri appartenenti a quel genere.
La query dovrà restituire il risultato ordinato alfabeticamente per genere.

3) Ordinamento risultati (ORDER BY)
Scrivere una query che elenchi tutti i libri pubblicati dopo l’anno 2010 ordinati in modo decrescente per anno di pubblicazione e, in caso di anno uguale, in ordine crescente per prezzo.

*/
