import json

from rest_framework.test import APITestCase
from rest_framework import status

from secret.models import Secret
from secret.tasks import delete_open_secret


class SecretAPITestCase(APITestCase):
    """
    TestCase to check the Secrets work
    """
    def setUp(self):
        """
        SetUp default Secret (is open) in testDB
        """
        self.secret = Secret.objects.create(
            text='test text',
            key='test key',
            secret_key='secret_key',
            lifetime='30_min',
            is_open=True,
        )

    def test_create_and_check_new_secret(self):
        """
        Test to check create and open Secret
        """
        # new Secret SetUp data
        secret_data = {
            'text': 'my text',
            'key': 'my key',
            'lifetime': '1_hour',
        }
        data = json.dumps(secret_data)
        # request/response for create new Secret
        response = self.client.post(
            '/secret/generate/',
            data=data,
            content_type='application/json',
        )

        # checking response for new Secret
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # response (-> secret_key) to created Secret
        secret_key_data = response.json()
        # request/response for open created Secret
        response_2 = self.client.get(
            f'/secret/secrets/{secret_key_data}',
        )

        # checking response for created Secret
        self.assertEquals(response_2.status_code, status.HTTP_200_OK)

    def test_delete_open_secret(self):
        """
        Test to check deleting open Secret
        """
        # count create by SetUp opened Secrets
        queryset_setup_count = Secret.objects.all().count()
        # deleting opened Secrets by shared_task
        delete_open_secret()
        # checking Secrets in testDB
        queryset_2 = Secret.objects.all()
        # empty queryset
        queryset_check = []

        # checking started Secrets in testDB
        self.assertEqual(queryset_setup_count, 1)

        # checking Secrets in testDB with empty queryset
        self.assertQuerySetEqual(queryset_2,queryset_check)
