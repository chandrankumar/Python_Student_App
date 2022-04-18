# Python_Student_App
Django framework of School Management System

python -m django startproject student-app

python manage.py runserver

python manage.py startapp userprofile

DB setup
python manage.py migrate

python manage.py createsuperuser

username: admin
password: admin



After create and activate Virtual Environment then run the django command for module installation
python -m venv env
env\Scripts\activate.bat

pip install django
pip install django-crispy-forms


python manage.py makemigrations

Docker mysql permission for not allowed connection
update mysql.user set host='%' where user ='root'
flush privileges;