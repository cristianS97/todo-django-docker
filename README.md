# todo-django-docker

## Docker
1. Crear imagen: docker build -t todo-django-docker-api .
2. Correr imagen: docker run --name backend -p 8000:8000 -d todo-django-docker-api

## Docker compose
* Ejecutar: docker-compose -f backend.yml up -d
* Bajar servicio: docker-compose -f backend.yml down
