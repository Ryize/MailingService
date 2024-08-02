# MailingService
Сервис для отправки писем или создания массовых рассылок. Использует Celery+Redis

## Deploy locally:

Клонируйте репозиторий и перейдите в установленную директорию:
```
git clone https://github.com/Ryize/MailingService.git
cd MailingService
```

Установите requirements:
```
pip3 install -r requirements.txt
```
> Если вы развертываете проект на сервере или хостинге с доменом, то укажите это в настройках проекта в переменной ALLOWED_HOSTS (DjangoBlog.settings)
```
ALLOWED_HOSTS = ['127.0.0.1']
```


Установите и запустите Celery и Redis. Проверьте настройки в MailingService.settings
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

Войдите в почту с помощью django
https://pocoz.gitbooks.io/django-v-primerah/content/glava-2-uluchshenie-bloga-s-pomoshyu-rasshirennyh-vozmozhnostej/otpravka-postov-na-e-mail/otpravka-e-mail-v-django.html

> Если режим DEBUG отключен (False), сайт перестанет автоматически собирать статику и медиа, не забудьте настроить Nginx/Apache
```
DEBUG = True
```

Соберите статику и запустите миграции:
```
python3 manage.py collectstatic
python3 manage.py migrate
```

Запустите проект:
```
python3 manage.py runserver
```

> Технологии, использованные в проекте: Python 3, Django, Celery, Redis.
