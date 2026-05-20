from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from core.models import LinkModel


class CrudTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='teste',
            email='teste@cps.sp.gov.br',
            password='123'
        )

        self.client.login(
            username='teste',
            password='123'
        )

    def test_criar_link(self):

        self.client.post(
            reverse('create'),
            {
                'titulo':'Google',
                'link':'https://google.com',
                'observacao':'Busca'
            }
        )

        self.assertEqual(
            LinkModel.objects.count(),
            1
        )

    def test_listar_links(self):

        LinkModel.objects.create(
            titulo='Google',
            link='https://google.com'
        )

        response = self.client.get(
            reverse('home')
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_update(self):

        link = LinkModel.objects.create(
            titulo='A',
            link='https://a.com'
        )

        self.client.post(
            reverse(
                'update',
                args=[link.id]
            ),
            {
                'titulo':'Novo',
                'link':'https://novo.com',
                'observacao':''
            }
        )

        link.refresh_from_db()

        self.assertEqual(
            link.titulo,
            'Novo'
        )

    def test_delete(self):

        link = LinkModel.objects.create(
            titulo='A',
            link='https://a.com'
        )

        self.client.post(
            reverse(
                'delete',
                args=[link.id]
            )
        )

        self.assertEqual(
            LinkModel.objects.count(),
            0
        )