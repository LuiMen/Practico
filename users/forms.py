from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class UserLoginForm(forms.Form):
    username = forms.CharField(label=_('Username'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError(_('Invalid credentials'))

        return super().clean()
