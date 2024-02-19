docker:
	docker build -t querymaster:alfa .
	docker run --name querymaster -d -p 8080:8080 querymaster:alfa
