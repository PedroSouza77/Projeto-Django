from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class IndexTemplateTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='teste@cps.sp.gov.br',
            email='teste@cps.sp.gov.br',
            password='123456'
        )

    def test_template_index(self):

        self.client.login(
            username='teste@cps.sp.gov.br',
            password='123456'
        )

        response = self.client.get(
            reverse('home'),
            follow=True
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            'index.html'
        )