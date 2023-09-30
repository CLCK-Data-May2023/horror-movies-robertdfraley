SELECT id "Movie_ID", name "Movie_Title", imdb_rating "Rating"
FROM movies
WHERE genre = 'horror'
AND year <= 1985
ORDER BY imdb_rating DESC
LIMIT 3;