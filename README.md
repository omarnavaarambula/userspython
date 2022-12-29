# Django, Pandas, Flask, JET

## Models.py -> Serializers.py -> Views.py -> Urls.py

crear archivo .txt
requirements.txt
con las dependencias


Django==3.2

djangorestframework==3.12.4

certifi==2022.9.24

charset-normalizer==2.1.1

click==8.1.3

Flask==2.1.3

Flask-API==3.0.post1

idna==3.4

importlib-metadata==4.12.0

itsdangerous==2.1.2

Jinja2==3.1.2

requests==2.28.1

urllib3==1.26.13


PyJWT==1.7.1

_________________________________

crear el venv


python3 -m venv .venv

activa la carpeta venv
source .venv/bin/activate


python3 -m pip install --upgrade pip

<!-- instala todos los requerimientos que se ocupan en el proyecto -->
dependencias
pip install -r requirements.txt

crar proyecto 
django-admin startproject app

________________________________________

entrar a carpeta app
cd app


_______
python manage.py startapp core

que tiene core
tiene parte donde crear nuestros modelos
___________________________

en la misma direccion de la carpeta app
comando
python manage.py runserver


se crean archivos docker

dokerfile


(codigo)
FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /app
COPY ./app /app

EXPOSE 8000


y doker-compose
(codigo)

version: "3.6"
services:
  
    app:
  
      build: 
        context: .
      ports:
        - "8000:8000"
      volumes:
      - ./app:/app
      command: >
        sh -c "python manage.py makemigrations &&
               python manage.py migrate &&
               python manage.py runserver 0.0.0.0:8000"


 
para ejecutar el archivo se ejecuta en carpeta raiz


ls -l (para ver carpetas y archivos )

ejecutar en terminal 

docker build .


docker-compose up



ir a setting.py
app/app/

buscar ALLOWED_HOST = [0.0.0.0]


__________________________________

agregar en el archivo settings.py
en la parte de INSTALLED_APPS 

'core',
'rest_framework',

____________________________________

en archivo urls.py (carpeta app/app)
(codigo)

from django.urls import path, include

urlpatterns = [
    path('v1/', include('core.urls')),

crear archivo en carpeta core 
urls.py


crear archivo en carpeta core

srializer.py

ir archivo views.py

______________________________
________________________
__________
________
______
_

para el entregable ejecutar app.py
instalar Flaks,pandas

pip install flask
pip install pandas


____________

test

importar pandas

pip install pytest

run test

pytest -v

en settings.py esta en app/app
agregar al final

AUTH_USER_MODEL = 'core.User'

siguen los serializadores

serializer.py

_________________

kill server code 
sudo lsof -t -i tcp:8000 | xargs kill -9

__________________________________
el archivo models.py

________
en settings.py esta en app/app
agregar 

AUTH_USER_MODEL = 'core.User'

siguen los serializadores

serializer.py

_________________

runnig app si no corre con docker

1.-python manage.py makemigrations 

2.-python manage.py migrate 

3.-python manage.py runserver 0.0.0.0:8000


_____________________________




## 1.- crea usuario name,email y password (POST)
/v1/register

![alt text](https://github.com/omarnavaarambula/userspython/blob/main/img/1.createUserPost.png)

## 2.- hace login al usuario con email y password(desifrado en JWT)(POST)
/v1/login

![alt text](https://github.com/omarnavaarambula/userspython/blob/main/img/2.loginusuarioPost.png)

## 3.- se ve la informacion del usuario con el password desifrado (GET)
/v1/user

![alt text](https://github.com/omarnavaarambula/userspython/blob/main/img/3.usuarioGet.png)

## 4.- logout de usuario, email y password (POST)
/v1/logout

![alt text](https://github.com/omarnavaarambula/userspython/blob/main/img/4.logoutPost.png)

## 5.- confirmacion de que el usuario realizo logout (GET)
/v1/user
![alt text](https://github.com/omarnavaarambula/userspython/blob/main/img/5.confirmationLogoutuser.png)



