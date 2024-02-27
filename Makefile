docker:
	docker build -t eurekaquery:alfa .
	docker run --name eurekaquery -d -p 8080:8080 eurekaquery:alfa
