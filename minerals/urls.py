from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'random/$', views.random, name='random'),
]