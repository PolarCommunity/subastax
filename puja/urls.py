from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^puja/$', ListaPuja.as_view(),name ="ListaPuja"),
    url(r'^puja/crear/(?P<pk>\d+)/$', CreatePuja, name="CreatePuja"),
    url(r'^puja/crear/articulo$', CrearArticulo.as_view(), name="CrearArticulo"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
