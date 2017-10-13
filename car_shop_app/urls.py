from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # Просмотр
    url(r'^(?P<entity>[a-z]+)/$', views.show),
    # Авто
    url(r'^cars/new/$', views.cars_new, name='cars_new'),
    url(r'^cars/(?P<id>\d+)/edit/$', views.cars_edit, name='cars_edit'),
    # Клиенты
    url(r'^customers/new/$', views.customers_new, name='customers_new'),
    url(r'^customers/(?P<id>\d+)/edit/$', views.customers_edit, name='customers_edit'),
    # Аксессуары
    url(r'^accessories/new/$', views.accessories_new, name='accessories_new'),
    url(r'^accessories/(?P<id>\d+)/edit/$', views.accessories_edit, name='accessories_edit'),
    # Удаление
    url(r'^(?P<entity>[a-z]+)/delete/(?P<id>\d+)/$', views.delete),
]