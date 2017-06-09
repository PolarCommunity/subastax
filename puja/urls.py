from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^puja/$', ListaPuja.as_view(),name ="ListaPuja"),
    url(r'^puja/crear/articulo$', CrearArticulo, name="CrearArticulo"),
    url(r'^puja/detalle/(?P<pk>\d+)$', detalle_puja, name="detalle_puja"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
