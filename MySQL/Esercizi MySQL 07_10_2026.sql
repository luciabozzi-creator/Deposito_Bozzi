-- ESERCIZIO HAVING

/*
USE world;
SELECT Continent,
    COUNT(*) AS n_paesi, 
    SUM(Population) AS Popolazione
FROM country
GROUP BY Continent
HAVING COUNT(*) > 40;

*/

-- SHOW DATABASES LIKE 'sakila';

-- PARTE 1 – RIPASSO SELECT E WHERE
 
-- 1. DISTINCT e COUNT DISTINCT – Elencare, senza ripetizioni, i rating presenti nella tabella film. In una seconda query, contare quanti cognomi diversi ci sono tra gli attori.

SELECT DISTINCT rating
FROM film;

-- 2. AND, OR, NOT, IN – Mostrare i film con rating 'PG-13' e rental_rate pari a 4.99, oppure con durata inferiore a 50 minuti, usando parentesi esplicite. 
-- In una seconda query, mostrare i film con durata inferiore a 60 minuti il cui rating non è 'G' né 'PG' (usare NOT IN).

SELECT title, rating, rental_rate, length
FROM film
WHERE (rating = 'PG-13' AND rental_rate = 4.99) OR (length < 50);

SELECT title, length, rating
FROM film
WHERE length < 60
AND rating NOT IN ('G', 'PG');

-- 3. LIKE e _ – Trovare gli attori il cui cognome inizia con 'S' e i clienti il cui nome è composto da esattamente 4 lettere.

SELECT first_name, last_name
FROM actor
WHERE last_name LIKE 'S%';

SELECT first_name, last_name
FROM customer
WHERE first_name LIKE '____';

-- 4. BETWEEN e IS NULL – Mostrare i pagamenti con importo tra 5 e 7 effettuati nel mese di luglio 2005, 31 luglio compreso (payment_date contiene anche l'orario). In una seconda query, mostrare i noleggi non ancora restituiti.

SELECT payment_id, amount, payment_date
FROM payment
WHERE amount BETWEEN 5 AND 7
AND payment_date >= '2005-07-01'
AND payment_date < '2005-08-01';

SELECT rental_id, rental_date, return_date
FROM rental
WHERE return_date IS NULL;

-- 5. ORDER BY, LIMIT, ALIAS – Mostrare i 10 film con replacement_cost più alto, a parità ordinati per titolo, con le colonne "Titolo", "Costo" e "Ore" (length / 60.0, arrotondata a 2 decimali).

SELECT title AS Titolo,
       replacement_cost AS Costo,
       ROUND(length / 60.0, 2) AS Ore
FROM film
ORDER BY replacement_cost DESC, title ASC
LIMIT 10;

-- 6. AGGREGAZIONI – Mostrare durata minima, massima e media dei film. In una seconda query, mostrare il numero di pagamenti e l'incasso totale.

SELECT MIN(length) AS Durata_Minima,
       MAX(length) AS Durata_Massima,
       AVG(length) AS Durata_Media
FROM film;

SELECT COUNT(*) AS Numero_Pagamenti,
       SUM(amount) AS Incasso_Totale
FROM payment;


-- PARTE 2 – JOIN
-- 7. JOIN MULTIPLO – Mostrare nome, cognome, città e paese dei clienti che vivono in 'Italy'.

SELECT customer.first_name,
       customer.last_name,
       city.city,
       country.country
FROM customer
INNER JOIN address
    ON customer.address_id = address.address_id
INNER JOIN city
    ON address.city_id = city.city_id
INNER JOIN country
    ON city.country_id = country.country_id
WHERE country.country = 'Italy';

-- 8. JOIN SU TABELLE PONTE – Mostrare titolo e categoria dei film in cui ha recitato PENELOPE GUINESS.

SELECT film.title,
       category.name AS Categoria
FROM actor
INNER JOIN film_actor
    ON actor.actor_id = film_actor.actor_id
INNER JOIN film
    ON film_actor.film_id = film.film_id
INNER JOIN film_category
    ON film.film_id = film_category.film_id
INNER JOIN category
    ON film_category.category_id = category.category_id
WHERE actor.first_name = 'PENELOPE' AND actor.last_name = 'GUINESS';

-- 9. LEFT / RIGHT JOIN – Trovare con LEFT JOIN e IS NULL i film non presenti in magazzino. Riscrivere poi la query con RIGHT JOIN.

SELECT film.title
FROM film
LEFT JOIN inventory
ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IS NULL;

SELECT film.title
FROM inventory
RIGHT JOIN film
ON inventory.film_id = film.film_id
WHERE inventory.inventory_id IS NULL;

-- 10. CROSS JOIN – Generare tutte le combinazioni tra i negozi (store_id) e i nomi delle categorie.

SELECT store.store_id,
       category.name AS Categoria
FROM store
CROSS JOIN category;
 
-- PARTE 3 – GROUP BY E HAVING
 
11. GROUP BY + JOIN – Per ogni categoria, mostrare il numero di film e la durata media arrotondata a 1 decimale, ordinando dalla categoria più numerosa.
12. HAVING – Mostrare le categorie con più di 65 film.
13. GROUP BY SU PIÙ COLONNE – Contare i film per categoria e rating, mostrando solo le combinazioni con almeno 15 film.
14. WHERE + GROUP BY + HAVING – Considerando solo i film con rating 'R', mostrare le categorie con durata media superiore a 120 minuti.
15. HAVING + SUM – Mostrare i clienti (id, nome, cognome) che hanno speso in totale più di 180, ordinati per spesa decrescente.
16. HAVING + COUNT – Mostrare gli attori (id, nome, cognome) che hanno recitato in almeno 35 film. Attenzione: esistono attori omonimi.
17. COUNT(*) vs COUNT(colonna) – Per ogni cliente, mostrare il numero di noleggi totali e di noleggi restituiti, usando COUNT(*) e COUNT(return_date). Mostrare solo i clienti con almeno un noleggio non restituito.
18. GROUP BY SU DATE – Mostrare numero di pagamenti e incasso per ogni anno e mese.
19. JOIN LUNGO + GROUP BY – Mostrare l'incasso totale per categoria, in ordine decrescente (payment → rental → inventory → film → film_category → category).
20. COUNT DISTINCT IN GROUP BY – Per ogni negozio, mostrare l'incasso totale dei pagamenti dei suoi clienti (in base a customer.store_id) e il numero di clienti. Attenzione a contare i clienti e non i pagamenti.
21. TOP N – Mostrare i 5 film più noleggiati, con titolo e numero di noleggi. A parità di noleggi, ordinare per titolo.
 
PARTE 4 – UNION, EXISTS, ANY, ALL
 
22. UNION e UNION ALL – Creare un elenco unico dei nomi (first_name) di attori e clienti, senza duplicati e in ordine alfabetico. Ripetere poi con UNION ALL e confrontare il numero di righe.
23. UNION CON COLONNA TIPO – Elencare nome e cognome di attori, clienti e staff, con una colonna che indichi 'Attore', 'Cliente' o 'Staff'.
24. UNION + AGGREGATI – Mostrare il numero di film per rating e aggiungere, con UNION ALL, una riga 'TOTALE' con il conteggio complessivo.
25. EXISTS – Mostrare i clienti che hanno noleggiato almeno un film nel mese di febbraio 2006.
26. NOT EXISTS – Mostrare i film che non sono mai stati noleggiati. Nota: rental è collegata a film tramite inventory.
27. EXISTS CORRELATO – Mostrare i clienti che hanno noleggiato almeno un film della categoria 'Horror'.
28. EXISTS vs IN – Riscrivere l'esercizio 27 usando IN al posto di EXISTS.
29. NOT EXISTS CON JOIN – Mostrare gli attori che non hanno mai recitato in film della categoria 'Action'.
30. ANY – Mostrare titolo e durata dei film più lunghi di almeno uno dei film della categoria 'Children'.
31. ALL – Mostrare titolo e durata dei film più lunghi di tutti i film della categoria 'Children'. Riscrivere poi gli esercizi 30 e 31 usando MIN e MAX.
32. ALL CON AGGREGATI – Usando >= ALL, mostrare il cliente (o i clienti) con la spesa totale più alta.
33. ALL vs LIMIT – Usando >= ALL, mostrare il film (o i film) noleggiati più volte e confrontare il risultato con l'esercizio 21.
*/

