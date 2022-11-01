# online-shop
This is a simple project for training django rest framework. 
This project made by DRF and use celery for sending email.
And also used jwt (JSON Web Token Authorization) for authorizing users. 

## Install:
For using this project you must install python3 and use virtualenv.
* Create virtual env.
```
python -m venv venv
```
* Activate virtual env.
```
source venv/bin/activate
```
* Install requirements
```
pip install -r requirements.txt
```

## Complete .env file
Due to the sensitive parts of the settings, I moved them to a protected file.\
To edit it, you need to create a file named `.env` in the root of the program.
And move all the contents of the `.env-example` file to `.env`.
Then complete the `.env` file with your information.
```
SECRET_KEY = 'set your secret key'

EMAIL_HOST = 'set email host'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'set email host username'
EMAIL_HOST_PASSWORD = 'set email host password'

CELERY_BROKER_URL = 'set result_url'
CELERY_RESULT_BACKEND = 'set result backend'
```
## Usage
```
python manage.py runserver
```

## Tips
Swagger tool is used for easier use of APIs.
```
http://localhost:8000/schema/swagger-ui/
http://localhost:8000/schema/redoc/
```
And also you can download all API docs...
```
http://localhost:8000/schema/
```
