IMAGE_NAME = etl-livros
CONTAINER_NAME = etl-livros
REPOSITORY_NAME = etl-livros
PORT = 8080

ifneq (,$(wildcard .env))
    include .env
    export
endif

docker: 
	@echo "Construindo a imagem Docker..."
	@docker build \
	--no-cache \
	-f Dockerfile \
	-t $(IMAGE_NAME) .

run:
	@echo "Executando o container Docker..."
	@docker run -d --name $(CONTAINER_NAME) $(IMAGE_NAME)

clean:
	@echo "Limpando imagens e contêineres Docker..."
	@docker stop $(CONTAINER_NAME) || true
	@docker rm $(CONTAINER_NAME) || true
	@docker rmi $(IMAGE_NAME) || true
