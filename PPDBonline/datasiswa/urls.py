from django.conf.urls import url

from . import views

urlpattersn = [
    url(r'^$',views.index, name='index'),
    
]