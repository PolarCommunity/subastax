from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^usuario/$', Register, name ="Register"),
    url(r'^cerrar/$', Logout, name ="Logout"),
    url(r'^$', Home, name ="home"),
    url(r'^password/', ChangePassword, name="ChangePassword"),
    url(r'^home$', Home, name ="home"),
]
