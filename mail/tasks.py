from MailingService.Celery import app

from .service import send_email, send_mass_email


@app.task(bind=True, default_retry_delay=60, max_retries=10)
def a_send_mail(self, *args, **kwargs):
    result = send_email(*args, **kwargs)
    if result['status'] == 'error':
        print(f"Произошла ошибка: {result['message']}")
        raise self.retry()


@app.task(bind=True, default_retry_delay=120, max_retries=10)
def a_send_mass_mail(self, *args, **kwargs):
    result = send_mass_email(*args, **kwargs)
    if result['status'] == 'error':
        print(f"Произошла ошибка при массовой рассылке: {result['message']}")
        raise self.retry()
