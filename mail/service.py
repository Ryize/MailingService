from django.core.mail import send_mail


def send_email(email: str, subject: str, message: str, from_email: str) -> dict:
    try:
        send_mail(recipient_list=[email], subject=subject, message=message, from_email=from_email)
        return {'status': 'ok'}
    except Exception as exc:
        return {'status': 'error', 'message': str(exc)}
