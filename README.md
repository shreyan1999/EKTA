# EKTA
Crowd sourcing solutions


command for running this project

python is required

check python --version or python3 --version

pip install -r requirements.txt or pip3 install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
NOTE: By default run in 8000 port
http://localhost:8000/

if you want to run on your ip
python manage.py runserver 0.0.0.0:PORT

PORT like -- 8000, 8080 etc..