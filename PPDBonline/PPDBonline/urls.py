
from django.contrib import admin
from django.conf.urls import url, include

from . import views
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^datasiswa/', include('datasiswa.urls'.namespace='datasiswa')),
    url('admin/', admin.site.urls),
]
