from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, resolve
from ExamenPractico.settings import exempt_urls


def login_exempt(view):
    view.login_exempt = True
    return view


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if getattr(view_func, 'login_exempt', False):
            return

        if request.user.is_authenticated:
            return

        if resolve(request.path_info).url_name in exempt_urls:
            return

        return login_required(function=view_func, login_url=reverse_lazy('login'))(request, *view_args, **view_kwargs)
