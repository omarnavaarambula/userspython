## Django

crear archivo .txt
requirements.txt
con las dependencias


Django==3.2
djangorestframework==3.12.4

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

