# Variables declaration ---------------------------------------------------------------------------------------------- #
PROFILE  = "development"
SERVICE  = "counter-service"
VERSION  = `git describe --tags --abbrev=0`

# Docker ------------------------------------------------------------------------------------------------------------- #
.PHONY: docker/build
docker/build:
	docker build --file Dockerfile --tag $(SERVICE):$(VERSION) .

# Docker-Compose ----------------------------------------------------------------------------------------------------- #
.PHONY: docker-compose/down
docker-compose/down:
	docker-compose --file deployment/docker/docker-compose.yaml --profile $(PROFILE) down --volumes

.PHONY: docker-compose/log
docker-compose/log:
	docker-compose --file deployment/docker/docker-compose.yaml logs -f --tail 10

.PHONY: docker-compose/pull
docker-compose/pull:
	docker-compose --file deployment/docker/docker-compose.yaml --profile $(PROFILE) pull

.PHONY: docker-compose/up
docker-compose/up:
	docker-compose --file deployment/docker/docker-compose.yaml --profile $(PROFILE) up -d

# Gunicorn ----------------------------------------------------------------------------------------------------------- #
.PHONY: gunicorn/run
gunicorn/run:
	gunicorn main:application --workers 1 --bind 0.0.0.0:8000
