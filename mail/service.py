from django.core.mail import send_mail, send_mass_mail


def send_email(email: str, subject: str, message: str, from_email: str) -> dict:
    try:
        send_mail(recipient_list=[email], subject=subject, message=message, from_email=from_email)
        return {'status': 'ok'}
    except Exception as exc:
        return {'status': 'error', 'message': str(exc)}


def send_mass_email(emails: list, subject: str, message: str, from_email: str) -> dict:
    try:
        messages = ([subject, message, from_email, i] for i in emails)
        send_mass_mail(messages)
        return {'status': 'ok'}
    except Exception as exc:
        return {'status': 'error', 'message': str(exc)}
