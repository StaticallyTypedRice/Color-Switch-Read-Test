@echo off

echo Setting up Color Switch Read Test...
echo This script will install Django, run migrations, collect static files and create a superuser.
echo Make sure to run this script in an activated virtualenv if you wish to use one.

pause

pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
