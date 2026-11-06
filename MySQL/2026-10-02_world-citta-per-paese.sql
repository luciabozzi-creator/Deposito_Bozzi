/*

Che cos'è SQL?

SQL significa "Structured Query Language" ed è un linguaggio che serve a gestire i database relazionali. 
Per il nostro corso stiamo utilizzando MySQL come RDBMS e MySQL Workbench come programma per scrivere le query.

3.Che cos'è una query in SQL e sotto quale forma il database restituisce i dati richiesti?

La query è una interrogazione al database e i risultati vengono restituiti in visualizzazione nel pannello piu basso nella sezione "Output/Result" in MySQL Workbench.

4.A cosa serve l'istruzione SELECT e cosa indica il simbolo dell'asterisco (*) quando scriviamo ad esempio: SELECT * FROM city;?

L'istruzione SELECT serve a restituire i dati presenti contenuti in una tabella di un database.
Nell'esempio l'asterisco * indica di voler vedere in output tutti i campi o colonne della tabella city e i relativi record senza ulteriori condizioni.

5.A cosa serve la clausola LIMIT in MySQL e per quale motivo viene quasi sempre utilizzata in combinazione con la clausola ORDER BY? Fai un esempio pratico in cui usare "LIMIT" senza "ORDER BY" produrrebbe un risultato privo di valore informativo certo.

La clausola LIMIT in MySQL serve a "Limitare" o ad indicare il numero massimo di righe da visualizzare. 
Viene utilizzata per gestire grandi tabelle con migliaia di record oppure per stilare insieme ad "ORDER BY" una classifica come la TOP 10 ottenendo in risultato un elenco interpretabile come una classifica di un particolare indicatore in ordine crescente "ASC" o decrescente "DESC".
Senza "ORDER BY" il criterio di ordinamento non sarebbe ben dichiarato e quindi questa clausola mostrerebbe la selezione dall'alto verso il basso i primi "n" record indicati contenuti dalla tabella.

6.Spiega la differenza fondamentale tra il metacarattere percentuale (%) e il metacarattere trattino basso (_) utilizzati con l'operatore LIKE.
Scrivi inoltre il predicato LIKE per trovare i codici che iniziano con la lettera "A" e sono lunghi in tutto esattamente 4 caratteri.

Esercizio LIKE: LIKE 'A___', in questo caso il metacarattere "_" seleziona fra i valori esattamente un singolo carattere e se ne indicano 4.
Esercizio LIKE: LIKE 'A%', in questo caso il metacarattere "%" seleziona tutti i valori che iniziano con la A.
La differenza fra i due è che "%" non specifica quanti caratteri devono essere presenti prima o dopo "%" mentre il metacarattere "_" si.

SELECT Codice
FROM Prodotti
WHERE Codice LIKE 'A%';

SELECT Codice
FROM Prodotti
WHERE Codice LIKE 'A___';


7.Descrivi con parole semplici la differenza di comportamento tra una INNER JOIN e una LEFT JOIN quando colleghiamo la tabella Clienti (tabella di sinistra) alla tabella Ordini (tabella di destra).

Cosa viene visualizzato a schermo per i clienti che non hanno mai effettuato ordini in ciascuno dei due casi?

Se si utilizza una "INNER JOIN" vengono elencati in output solo i clienti per i quali esiste almeno un ordine.
Quindi se un cliente non ha mai effettuato ordini non verrà elencato perchè si selezionano solo i recordi in comune alle due tabelle.

Se si utilizza una "LEFT JOIN" vengono elencati tutti i clienti presenti, anche quelli che non hanno mai effettuato un ordine.
In questo caso le informazioni non presenti della tabella Ordini relative a questi clienti che non hanno mai ordinato, verranno lasciate vuote con il valore NULL.

*/

/*
8.Considera la tabella city del database world; 
Richiesta: Scrivere una query SQL che calcoli ed estragga in un'unica riga le seguenti statistiche demografiche sulle città:   
   
Il numero complessivo di città individuate con alias NumeroCitta.
   
La popolazione minima registrata con alias PopolazioneMinima.
   
La popolazione massima registrata con alias PopolazioneMassima.
   
La popolazione media delle città considerate, arrotondata all'intero più vicino con alias PopolazioneMedia.
   
Condizioni di filtro obbligatorie:   
   
Considerare solo le città situate in Italia, Spagna o Francia (CountryCode IN ('ITA', 'ESP', 'FRA')).
   
E il cui distretto/regione (District) inizia con la lettera 'M' (usare l'operatore LIKE).

*/

/*
USE world;
SELECT
    COUNT(*) AS NumeroCitta,
    MIN(Population) AS PopolazioneMinima,
    MAX(Population) AS PopolazioneMassima,
    ROUND(AVG(Population)) AS PopolazioneMedia
FROM city
WHERE CountryCode IN ('ITA', 'ESP', 'FRA')
AND District LIKE 'M%';
*/

/*
9.Considera le due tabelle collegate da chiave esterna:
   city 
   country 
   collegate tramite la relazione city.CountryCode = country.Code.   
   
   
Richiesta:
Scrivere una query SQL che colleghi le tabelle con una INNER JOIN e mostri:   
   
Il nome della città (city.Name) con alias NomeCitta,
   
Il nome della nazione (country.Name) con alias NomeNazione,
   
Il continente (country.Continent),
   
La popolazione della città (city.Population) con alias PopolazioneCitta.
   
   Condizioni di filtro e ordinamento:   
   
Considerare solo le nazioni appartenenti al continente europeo ('Europe').
   
Considerare unicamente le città con più di 1.000.000 di abitanti 
   
Ordinare i record in ordine decrescente di popolazione cittadina (dalla metropoli più popolosa a scendere).
   
Limitare l'output visualizzando esclusivamente le prime 5 città.
*/

/*
USE world;
SELECT
    city.Name AS NomeCitta,
    city.Population AS PopolazioneCitta,
    country.Name AS NomeNazione,
    country.Continent
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code
WHERE country.Continent = 'Europe'
AND city.Population > 1000000
ORDER BY city.Population DESC
LIMIT 5;
*/

/*

10.Considera le tabelle:
   country 
   city
   collegate tramite country.Code = city.CountryCode.   Nel database world vi sono alcuni territori o microstati (come l'Antartide o piccole isole) per i quali non risulta censita alcuna città nella tabella city.   Richiesta:
   Scrivere una query SQL che utilizzi una LEFT JOIN per trovare tutti i paesi del mondo che NON hanno alcuna città registrata nella tabella city.
   La query deve:   
   
Mostrare il codice dello stato (co.Code) con alias CodiceStato, il nome dello stato (co.Name) con alias NomeStato e il Continent con alias Continente.
   
Filtrare estraendo solo ed esclusivamente gli stati che non hanno alcuna corrispondenza nella tabella city (condizione con valore NULL).
   
Ordinare i risultati in ordine alfabetico per nome dello stato (co.Name ASC).
*/

/*
USE world;
SELECT
    co.Code AS CodiceStato,
    co.Name AS NomeStato,
    co.Continent AS Continente
FROM country AS co
LEFT JOIN city AS ci
    ON co.Code = ci.CountryCode
WHERE ci.CountryCode IS NULL
ORDER BY co.Name ASC;
*/

-- Quali sono le nazioni che hanno il maggior numero di città registrate nel database world?
USE world;
SELECT CountryCode, COUNT(*) AS NumeroCitta
FROM city
GROUP BY CountryCode
ORDER BY NumeroCitta DESC;

