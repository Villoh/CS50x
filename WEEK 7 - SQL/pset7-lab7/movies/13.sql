SELECT DISTINCT people.name
FROM people
INNER JOIN stars
ON people.id = stars.person_id
INNER JOIN movies
ON stars.movie_id = movies.id
WHERE people.name != 'Kevin Bacon' AND movies.title IN (

SELECT movies.title
FROM movies
INNER JOIN stars
ON movies.id = stars.movie_id
INNER JOIN people
ON stars.person_id = people.id
WHERE people.birth = 1958 AND people.name = 'Kevin Bacon');