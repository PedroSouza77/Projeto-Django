from django.test import TestCase
from core.models import LinkModel


class LinkModelTest(TestCase):

    def setUp(self):

        self.link = LinkModel.objects.create(
            titulo='Google',
            link='https://google.com',
            observacao='Busca'
        )

    def test_criacao(self):

        self.assertEqual(
            LinkModel.objects.count(),
            1
        )

    def test_str(self):

        self.assertEqual(
            str(self.link),
            'Google - https://google.com'
        )