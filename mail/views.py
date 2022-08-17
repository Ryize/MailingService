from django.http import JsonResponse
from mail.tasks import a_send_mail


def mail(request):
    email = "request.POST.get('email')"
    subject = "request.POST.get('subject')"
    message = "request.POST.get('message')"
    from_email = "request.POST.get('from_email')"
    if not (email and subject and message and from_email):
        return JsonResponse({'status': 'error', 'message': 'Not all parameters passed'})
    a_send_mail.delay(email, subject, message, from_email)
    return JsonResponse({'status': 'OK', 'message': 'Task created'})
