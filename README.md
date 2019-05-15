# recipe-management

## Download, setup and deploy the project

1. Download
    1.1. `~$ git clone https://github.com/guallo/recipe-management.git`
2. Setup
    2.1. `~$ cd recipe-management/`
    2.2. `recipe-management$ sudo apt-get install virtualenv`
    2.3. `recipe-management$ virtualenv -p python3 evns/1`
    2.4. `recipe-management$ source evns/1/bin/activate`
    2.5. `(1) recipe-management$ pip install -r requirements.txt`
    2.6. `(1) recipe-management$ ./manage.py makemigrations`
    2.7. `(1) recipe-management$ ./manage.py migrate`
    2.8. `(1) recipe-management$ ./manage.py createsuperuser --username admin --email admin@recipe-management.com`
3. Deploy
    3.1. `(1) recipe-management$ ./manage.py runserver`

## Browsable API

To browse the REST API open a browser at http://localhost:8000/api/

## Manage users

To manage users open a browser at http://localhost:8000/admin/ and login in with the initially created superuser (*admin*)
