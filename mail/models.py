from django.db import models


class Mail(models.Model):
    email = models.TextField()
    subject = models.CharField(max_length=256)
    message = models.CharField(max_length=2048)
    from_email = models.EmailField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    is_mass = models.BooleanField(default=False)
