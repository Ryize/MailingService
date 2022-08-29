from django.db import models


class Mail(models.Model):
    email = models.TextField(verbose_name="Почты(ы)")
    subject = models.CharField(max_length=256, verbose_name="Тема")
    message = models.CharField(max_length=2048, verbose_name="Сообщение")
    from_email = models.EmailField(max_length=64, verbose_name="Отправитель")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    is_mass = models.BooleanField(default=False, verbose_name="Массовая")

    def __str__(self):
        return f'{self.subject}. Массовая: {self.is_mass}'
