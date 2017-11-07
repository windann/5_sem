"""Определяет схемы url для my_first_site"""

from django.conf.urls import url
from . import views
from my_first_site.views import FlowersView, FlowerView


urlpatterns = [
    #Домашняя страница
    url(r'^$', views.index, name='welcome'),
    url(r'^variable/$', views.variable, name='variable'),
    url(r'^flowers/$', FlowersView.as_view(), name='flowers'),
    url(r'^flower/(?P<id>\d+)$', FlowerView.as_view(), name='flower')


]