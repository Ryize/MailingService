# MailingService
Service for sending letters or creating mass mailings. Uses Celery+Redis

## Deploy locally:

Clone the repository and go to installed folder:
```
git clone https://github.com/Ryize/MailingService.git
cd MailingService
```

Install requirements:
```
pip3 install -r requirements.txt
```
> If you are deploying a project to a server or hosting with a domain, then specify it in the project settings in the ALLOWED_HOSTS(DjangoBlog.settings) variable
```
ALLOWED_HOSTS = ['127.0.0.1']
```


Download and run Celery and Redis. Check the settings in MailingService.settings
```
REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility-timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
```

Login to mail with django
https://pocoz.gitbooks.io/django-v-primerah/content/glava-2-uluchshenie-bloga-s-pomoshyu-rasshirennyh-vozmozhnostej/otpravka-postov-na-e-mail/otpravka-e-mail-v-django.html

> If the DEBUG mode is disabled(False), the site will stop automatically collecting statics and media, do not forget to configure Nginx/Apache
```
DEBUG = True
```

Collect statics and run migrations:
```
python3 manage.py collectstatic
python3 manage.py migrate
```

Run the website:
```
python3 manage.py runserver
```

> Technologies used in the project: Python 3, Django, Celery, Redis.
