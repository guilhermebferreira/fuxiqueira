# Dependencias

A aplicação foi montada em container, com um docker-compose para subir o banco de dados, o backend e a interface

Então as dependencias necessárias são as do Docker e Docker-Compose


# Setup e Inicialização

	docker-compose build

	docker-compose up

## Aplicando migrations

Acesse o container do backend:

	docker exec -it fuxiqueira-api bash

Execute as migrations

	./manage.py migrate

Crie um usuario para acessar o painel admin	

	./manage.py createsuperuser

Use o exit para sair do bash do container

	exit

## Acessando a aplicação

A aplicação estrá disponivel nas portas configuradas no `docker-compose.yaml`

### api

	0.0.0.0:8010

### interface

	0.0.0.0:8081