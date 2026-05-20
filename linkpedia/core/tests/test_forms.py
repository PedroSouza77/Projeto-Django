from django.test import TestCase
from core.forms import LinkForm


class LinkFormTest(TestCase):

    def test_form_valido(self):

        form = LinkForm(
            data={
                'titulo':'Google',
                'link':'https://google.com',
                'observacao':'Busca'
            }
        )

        self.assertTrue(
            form.is_valid()
        )