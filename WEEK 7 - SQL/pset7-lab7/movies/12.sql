SELECT movies.title
FROM movies
INNER JOIN stars
ON movies.id = stars.movie_id
INNER JOIN people
ON stars.person_id = people.id
WHERE people.name = 'Bradley Cooper' AND movies.title IN (
SELECT movies.title
FROM movies
INNER JOIN stars
ON movies.id = stars.movie_id
INNER JOIN people
ON stars.person_id = people.id
WHERE people.name = 'Jennifer Lawrence');