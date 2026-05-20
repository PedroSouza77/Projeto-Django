from django.forms import ModelForm
from .models import LinkModel

class LinkForm(ModelForm):

    class Meta:
        model = LinkModel

        fields = (
            'titulo',
            'link',
            'observacao'
        )