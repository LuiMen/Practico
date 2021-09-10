from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

from ExamenPractico import settings
from users.forms import UserLoginForm, ChangePasswordForm


def login_view(request):
    title = _("Log in")
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/prospects/')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('/prospects/')

    return render(request, "registration/login.html", {
        "form": form,
        "title": title,
        "action": title,
    })


def logout_view(request):
    logout(request)
    return


def change_password(request):
    title = _('Change password')
    action = _('Change')
    form = ChangePasswordForm(request.POST or None, username=request.user.username)

    if form.is_valid():
        current = form.cleaned_data.get('current')
        password1 = form.cleaned_data.get('password1')
        if authenticate(username=request.user.username, password=current):
            user = User.objects.get(username=request.user.username)
            user.set_password(password1)
            user.save()

            login(request, authenticate(username=request.user.username, password=password1))

            return redirect('/prospects/')

    context = {
        "form": form,
        "title": title,
        "action": action,
    }

    return render(request, "register.html", context)


def password_reset(request):
    password_form = PasswordResetForm(data=request.POST or None)

    if password_form.is_valid():
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'email_template_name': strip_tags('registration/password_reset_email.html'),
            'subject_template_name': 'subject_reset_email.txt',
            'request': request,
            'html_email_template_name': 'registration/password_reset_email.html',
        }
        password_form.save(**opts)
        return redirect(reverse('password_reset_done'))

    context = {
        "form": password_form,
    }

    return render(request, "registration/password_reset_form.html", context)

