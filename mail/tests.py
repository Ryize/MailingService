import json

# from django.contrib.auth.models import User
# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework.test import APITestCase, force_authenticate
#
#
# class TestTest(APITestCase):
#     def setUp(self):
#         self.username = 'john_doe'
#         self.password = 'foobar'
#         self.user = User.objects.create(username=self.username, password=self.password)
#         self.client.force_authenticate(user=self.user)
#
#     def test_one(self):
#         user = User.objects.create(username='Jogn', password='1234')
#         v = {'email': 'dwjidwj@gmail.com', 'subject': 'eeffe', 'message': 'wjjwd', 'from_email': 'hejfe@gmail.com'}
#         a = self.client.post('/mail/', v, format='json')
#         print(a.status_code)
#         print(json.loads(a._container[0]))
