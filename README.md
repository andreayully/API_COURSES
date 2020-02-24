
# This is the API for Postman Course

It is a simple version of an API builded with Django and Django Rest Framework
using Docker.


# You can learn how to build APIs here:

- [Curso de API REST](https://platzi.com/clases/api-rest/)
- [Curso de Django](https://platzi.com/clases/django/)
- [Curso Avanzado de Django](https://platzi.com/clases/django-avanzado/)
- [Curso de Fundamentos de Docker](https://platzi.com/clases/docker/)

# How to run this project
- Install Docker and Docker Compose
- Execute `docker-compose up -d`: This command starts a local server with the API running over 8000 port.
- **WARNING:** Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`
- Get inside the docker container executing `docker exec -it postman-course_web_1 bash`
- Inside the docker container execute `python manage.py runserver 0.0.0.0:8000`