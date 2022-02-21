from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from agregatorapp.models import Log


class TestUserAuthorisation(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test_user', password='123454321qw')
        Log.objects.bulk_create([Log(ip_address="45.132.51.62",
                                     date_add='2020-12-19 15:23:12'),
                                 Log(ip_address="45.132.51.35",
                                     date_add='2020-12-30 15:23:12'),
                                 Log(ip_address="45.132.51.74",
                                     date_add='2021-01-05 15:23:12')])

    def test_get_token_auth_invalid(self):
        response = self.client.post('/api-token-auth/', {'username': 'test_user', 'password': '33243dsfgdgs'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_token_auth_valid(self):
        response = self.client.post('/api-token-auth/', {'username': 'test_user', 'password': '123454321qw'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_view_list_logs_without_token(self):
        response = self.client.get('/api/logs/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_view_list_logs_with_token(self):
        auth = self.client.post('/api-token-auth/', {'username': 'test_user', 'password': '123454321qw'})
        token = f'Token {auth.data.get("token")}'
        self.client.credentials(HTTP_AUTHORIZATION=token)
        response = self.client.get('/api/logs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), Log.objects.all().count())

    def test_filter_ip_address(self):
        self.auth_token_user()
        response = self.client.get('/api/logs/', {'ip_address': "45.132.51.35"})
        self.assertEqual(response.data.get('count'), 1)
        self.assertEqual(response.data.get('results')[0].get('ip_address'), "45.132.51.35")

    def test_filter_date_add(self):
        self.auth_token_user()
        response = self.client.get('/api/logs/', {'date_add': "2020-12-30"})
        self.assertEqual(response.data.get('count'), 1)
        self.assertTrue("2020-12-30" in response.data.get('results')[0].get('date_add'))

    def test_filter_date_range(self):
        self.auth_token_user()
        response = self.client.get('/api/logs/', {'date_range_after': "2020-12-30", 'date_range_before': "2021-01-05"})
        self.assertEqual(response.data.get('count'), 2)

    def auth_token_user(self):
        auth = self.client.post('/api-token-auth/', {'username': 'test_user', 'password': '123454321qw'})
        token = f'Token {auth.data.get("token")}'
        self.client.credentials(HTTP_AUTHORIZATION=token)
