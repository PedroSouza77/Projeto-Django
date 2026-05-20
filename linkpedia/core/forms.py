from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import LinkModel


class LoginForm(ModelForm):

    class Meta:

        model = User

        fields = (
            'email',
            'password'
        )


class LinkForm(ModelForm):

    class Meta:

        model = LinkModel

        fields = (
            'titulo',
            'link',
            'observacao'
        )