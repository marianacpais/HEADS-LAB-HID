# Development environment commands

app:
	python3 application.py

dev:
	pytest-watch

docker:
	docker build -f Dockerfile.dev -t eurekaquery:dev .
	docker run --name eurekaquery-dev --env-file ./.env -it -p 5001:5000 -v "$(PWD)":/app eurekaquery:dev

docker-bash:
	docker exec -w /app -it eurekaquery-dev /bin/bash

# Production environment commands
docker-prod:
	docker build -f Dockerfile.prod -t eurekaquery:prod .
	docker run --name eurekaquery-prod -d -p 8080:8080 eurekaquery:prod

# Stop and remove containers
docker-stop-dev:
	docker stop eurekaquery-dev
	docker rm eurekaquery-dev

docker-stop-prod:
	docker stop eurekaquery-prod
	docker rm eurekaquery-prod
