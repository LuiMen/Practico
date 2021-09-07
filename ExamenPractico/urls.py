from django.contrib import admin
from django.urls import path, include
from users.urls import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
