from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from http import HTTPStatus


class Login_OK_Test(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='teste@cps.sp.gov.br',
            email='teste@cps.sp.gov.br',
            password='123456'
        )

        self.resp = self.client.post(
            reverse('login'),
            {
                'email': 'teste@cps.sp.gov.br',
                'password': '123456'
            },
            follow=True
        )


    def test_response(self):

        self.assertEqual(
            self.resp.status_code,
            HTTPStatus.OK
        )


    def test_template_used(self):

        self.assertTemplateUsed(
            self.resp,
            'index.html'
        )


class Logout_Get_OK_Test(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='teste@cps.sp.gov.br',
            email='teste@cps.sp.gov.br',
            password='123456'
        )

        self.client.login(
            username='teste@cps.sp.gov.br',
            password='123456'
        )

        self.resp = self.client.get(
            reverse('logout'),
            follow=True
        )


    def test_response(self):

        self.assertEqual(
            self.resp.status_code,
            HTTPStatus.OK
        )


    def test_template_used(self):

        self.assertTemplateUsed(
            self.resp,
            'logout.html'
        )