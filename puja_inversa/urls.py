from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^puja_inv/$', ListaInvPuja.as_view(),name ="ListaInvPuja"),
    url(r'^puja_inv/crear/articulo$', CrearArticulo, name="CrearArticuloI"),
    url(r'^puja_inv/detalle/(?P<pk>\d+)$', detalle_puja_inv, name="detalle_puja_inv"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
