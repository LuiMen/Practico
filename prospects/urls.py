from django.conf.urls import url
from django.urls import path

from .views import prospects_list, ProspectsCreateView, prospect_view, approve_prospect_view

urlpatterns = [
    path('', prospects_list, name='prospects_list'),
    url(r'^registry/$', ProspectsCreateView.as_view(), name='register_prospect'),
    path('<int:pk>/', prospect_view, name='prospect_view'),
    url(r'^approve/$', ProspectsCreateView.as_view(), name='register_prospect'),
    url(r'^approve/(?P<pk>\d+)/$', approve_prospect_view, name='approve_prospect'),
]
