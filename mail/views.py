from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView

from mail.serializers import MailSerializer
from mail.tasks import a_send_mail


class MailView(GenericAPIView):
    serializer_class = MailSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MailSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse({'status': 'error', 'message': 'Переданы не все параметры. Или неверные данные.'})
        a_send_mail.delay(*serializer.data.values())
        return JsonResponse({'status': 'OK', 'message': 'Task created'})

# {
# 'email': 'cpv9908@gmail.com',
# 'subject': 'eefjfejfej',
# 'message': 'jfejfkefkef',
# 'from_email': ''shtitarenko@gmail.com
# }

# "{'email': 'cpv9908@gmail.com','subject': 'eefjfejfej','message': 'jfejfkefkef','from_email': 'shtitarenko@gmail.com'}"
