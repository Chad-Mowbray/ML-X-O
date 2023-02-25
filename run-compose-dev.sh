#!/bin/bash

# These environment variables are consumed by the docker-compose file.
export SECRET_KEY=abc123
export DEBUG=True

docker-compose -f docker-compose.dev.yml up --build -d

# make sure the postgres container is ready, the run migrations
sleep 10 
docker exec ml_tic_tac_toe-api-1  python /src/manage.py makemigrations 
docker exec ml_tic_tac_toe-api-1  python /src/manage.py migrate