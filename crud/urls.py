from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'principal.views.index'),
    url(r'^add/$', 'principal.views.agregar_producto'),
    url(r'^borrar/(?P<id_producto>\d+)$', 'principal.views.borrar_producto'),
    url(r'^editar/(?P<id_producto>\d+)$', 'principal.views.editar_producto'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^salir/$', 'principal.views.LogOut'),

)
