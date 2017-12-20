from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^twisters/?$', views.twisters, name='twisters'),
    url(r'^twister/?$', views.twister, name='twister'),
]