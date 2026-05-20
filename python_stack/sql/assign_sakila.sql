USE sakila;
SHOW TABLES;
SELECT c.first_name, c.last_name, c.email, a.address
FROM customer c
JOIN address a ON c.address_id = a.address_id
WHERE a.city_id = 312;

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, ca.name AS category
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category ca ON fc.category_id = ca.category_id
WHERE ca.name = 'Comedy';

SELECT a.actor_id, a.first_name, a.last_name, f.title, f.description, f.release_year
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE a.actor_id = 5;

SELECT c.first_name, c.last_name, c.email, a.address
FROM customer c
JOIN address a ON c.address_id = a.address_id
WHERE c.store_id = 1
AND a.city_id IN (1, 42, 312, 459);

SELECT f.title, f.description, f.release_year, f.rating, f.special_features
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
WHERE f.rating = 'G'
AND f.special_features LIKE '%Behind the Scenes%'
AND fa.actor_id = 15;

SELECT f.film_id, f.title, a.actor_id, a.first_name, a.last_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.film_id = 369;

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, ca.name AS category
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category ca ON fc.category_id = ca.category_id
WHERE ca.name = 'Drama'
AND f.rental_rate = 2.99;

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, ca.name AS category,
       a.first_name, a.last_name
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category ca ON fc.category_id = ca.category_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE ca.name = 'Action'
AND a.first_name = 'SANDRA'
AND a.last_name = 'KILMER';