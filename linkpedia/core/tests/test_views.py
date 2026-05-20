from django.test import TestCase
from django.urls import reverse


class ViewTest(TestCase):

    def test_home_sem_login(self):

        response = self.client.get(
            reverse('home')
        )

        self.assertEqual(
            response.status_code,
            302
        )