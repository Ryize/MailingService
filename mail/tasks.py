from MailingService.Celery import app

from .service import send_email


@app.task(bind=True, default_retry_delay=5, max_retries=10)
def a_send_mail(self, *args, **kwargs):
    result = send_email(*args, **kwargs)
    if result['status'] == 'error':
        print(f"Произошла ошибка: {result['message']}")
        raise self.retry()
