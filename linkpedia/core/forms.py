from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import LinkModel


from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(

        label='E-Mail:',

        widget=forms.EmailInput(

            attrs={

                'class':'form-control',

                'placeholder':'Digite seu e-mail institucional'

            }

        )

    )

    password = forms.CharField(

        label='Senha:',

        widget=forms.PasswordInput(

            attrs={

                'class':'form-control',

                'placeholder':'Digite sua senha'

            }

        )

    )


class LinkForm(forms.ModelForm):

    class Meta:

        model = LinkModel

        fields = '__all__'

        widgets = {

            'titulo': forms.TextInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Digite o título'

                }

            ),

            'link': forms.URLInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Digite o link'

                }

            ),

            'observacao': forms.Textarea(

                attrs={

                    'class':'form-control',

                    'placeholder':'Digite uma observação',

                    'rows':5

                }

            )

        }