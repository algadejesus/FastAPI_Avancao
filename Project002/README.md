
### Build image
```
docker build --progress=plain --no-cache -t project2 .
```

docker-compose up app

docker-compose run app


docker-compose stop postgresql
docker-compose up postgresql

docker-compose run --user 1000 app sh -c 'alembic init migrations'
docker-compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add categories table"'