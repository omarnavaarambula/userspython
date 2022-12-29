repaso django
semana4 
kill server code 
sudo lsof -t -i tcp:8000 | xargs kill -9

__________________________________
empesamos con el archivo models.py
empesando con los modelos

en settings.py esta en app/app
agregar al final

AUTH_USER_MODEL = 'core.User'

siguen los serializadores

serializer.py

_________________

runnig app si no corre con docker
1.-python manage.py makemigrations 
2.-python manage.py migrate 
3.-python manage.py runserver 0.0.0.0:8000



_____________________________

