TAG        := latest
IMAGE_NAME := panubo/sensu-result-proxy
REGISTRY   := docker.io

DOCKER_CONFIG := -v $(shell pwd)/config_example.yaml:/config/config.yaml -e CONFIG_FILE=/config/config.yaml

.PHONY: build bash run push
build:
	docker build -t ${IMAGE_NAME}:${TAG} .

bash:
	docker run --rm -it --name sensu-result-proxy -p 8080:8080 $(DOCKER_CONFIG) --entrypoint /bin/bash ${IMAGE_NAME}:${TAG}

run:
	docker run --rm -it --name sensu-result-proxy -p 8080:8080 $(DOCKER_CONFIG) ${IMAGE_NAME}:${TAG}

push:
	docker tag ${IMAGE_NAME}:${TAG} ${REGISTRY}/${IMAGE_NAME}:${TAG}
	docker push ${REGISTRY}/${IMAGE_NAME}:${TAG}
