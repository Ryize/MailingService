from django.http import JsonResponse
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView

from mail.models import Mail
from mail.serializers import MailSerializer, MassMailSerializer
from mail.tasks import a_send_mail, a_send_mass_mail


class MailView(GenericAPIView):
    serializer_class = MailSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MailSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse({'status': 'error', 'message': 'Переданы не все параметры. Или неверные данные.'})
        mailing_data_in_dict = {key: value for key, value in serializer.data.items()}
        Mail.objects.create(**mailing_data_in_dict)
        a_send_mail.delay(*serializer.data.values())
        return JsonResponse({'status': 'OK', 'message': 'Task mail created'})


class MassMailView(GenericAPIView):
    serializer_class = MassMailSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MassMailSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse({'status': 'error', 'message': 'Переданы не все параметры. Или неверные данные.'})
        mailing_data_in_dict = {key: value for key, value in serializer.data.items()}
        Mail.objects.create(**mailing_data_in_dict, is_mass=True)
        a_send_mass_mail.delay(*serializer.data.values())
        return JsonResponse({'status': 'OK', 'message': 'Task mass mail created'})


# {
# 'email': 'cpv9908@gmail.com',
# 'subject': 'eefjfejfej',
# 'message': 'jfejfkefkef',
# 'from_email': ''shtitarenko@gmail.com
# }

# "{'email': 'cpv9908@gmail.com','subject': 'eefjfejfej','message': 'jfejfkefkef','from_email': 'shtitarenko@gmail.com'}"