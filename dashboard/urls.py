from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user$', views.user, name='user'),
    url(r'^history$', views.history, name='history'),
    url(r'^logout$', views.logout, name='logout'),
]