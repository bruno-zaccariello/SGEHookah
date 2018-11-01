call python -m pip install --user -r requirements.txt
call python ./manage.py makemigrations --noinput
call python ./manage.py migrate
call python ./manage.py initadmin
call python ./manage.py runserver 0.0.0.0:8000