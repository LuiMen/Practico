from django.conf.urls import url
from .views import login_view, logout_view, change_password

urlpatterns = [
    url(r'^$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^change-password/$', change_password, name='change_password'),
]
