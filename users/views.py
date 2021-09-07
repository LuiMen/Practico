from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _

from users.forms import UserLoginForm


def login_view(request):
    title = _("Log in")
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/home')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('/home')

    return render(request, "registration/login.html", {
        "form": form,
        "title": title,
        "action": title,
    })


def logout_view(request):
    logout(request)
    return redirect('/')

