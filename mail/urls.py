from django.urls import path
from .views import *

urlpatterns = [
    path('', MailView.as_view()),
    path('mass/', MassMailView.as_view()),
]
