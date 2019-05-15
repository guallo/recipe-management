# recipe-management

## download, setup and deploy the project

~$ git clone https://github.com/guallo/recipe-management.git
~$ cd recipe-management/
recipe-management$ sudo apt-get install virtualenv
recipe-management$ virtualenv -p python3 evns/1
recipe-management$ source evns/1/bin/activate
(1) recipe-management$ pip install -r requirements.txt
(1) recipe-management$ ./manage.py makemigrations
(1) recipe-management$ ./manage.py migrate
(1) recipe-management$ ./manage.py createsuperuser --username admin --email admin@recipe-management.com
(1) recipe-management$ ./manage.py runserver

To browse the REST API open a browser at http://localhost:8000/api/

To manage users open a browser at http://localhost:8000/admin/ and login in with the previously created superuser (admin)
