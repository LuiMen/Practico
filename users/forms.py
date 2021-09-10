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


class ChangePasswordForm(forms.Form):
    username = ''
    current = forms.CharField(widget=forms.PasswordInput, label='Contraseña Actual', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Nueva Contraseña',
                                required=True, help_text='La contraseña debe incluir 4 o más caracteres')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña', required=True)

    def __init__(self, *args, **kwargs):
        self.username = kwargs.pop('username')
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        current = cleaned_data.get('current')
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        user = authenticate(username=self.username, password=current)
        if not user:
            raise forms.ValidationError(_('Incorrect current password.'))
        if p1 != p2:
            raise forms.ValidationError(_('Passwords does not match.'))

        return super().clean()
