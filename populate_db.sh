DIRECTOR="http://127.0.0.1:9002/"
MOVIE="http://127.0.0.1:9001/"
USER="http://127.0.0.1:9004/"
WATCHLIST="http://126.0.0.1:9003/"

curl -H "Content-Type: application/json" -d '{"id": 1, "name": "John"}' $DIRECTOR
curl -H "Content-Type: application/json" -d '{"id": 2, "name": "Mike"}' $DIRECTOR
curl -H "Content-Type: application/json" -d '{"id": 3, "name": "Jean"}' $DIRECTOR

curl -H "Content-Type: application/json" -d '{"id": 1, "name": "Yadollah"}' $USER
curl -H "Content-Type: application/json" -d '{"id": 2, "name": "Soraya"}' $USER

curl -H "Content-Type: application/json" -d '{"id": 1, "name": "Movie 1", "director_id": 1}' $MOVIE
curl -H "Content-Type: application/json" -d '{"id": 2, "name": "Movie 2", "director_id": 2}' $MOVIE
curl -H "Content-Type: application/json" -d '{"id": 3, "name": "Movie 3", "director_id": 2}' $MOVIE
curl -H "Content-Type: application/json" -d '{"id": 4, "name": "Movie 4", "director_id": 2}' $MOVIE

echo ""
