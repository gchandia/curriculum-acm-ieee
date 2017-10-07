from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'admin/invitaciones$', views.invitaciones, name='invitaciones'),
    url(r'admin/crear_encuesta$', views.crear_encuesta, name='crear encuesta'),
    url(r'admin/config$', views.config, name='configuracion'),
    url(r'encuesta_curso_1$', views.informacion_curso, name='informacion curso'),
    url(r'admin/home$', views.admin_home, name='home'),
    url(r'encuesta_curriculum$', views.encuesta, name='encuesta'),
    url(r'solicitar_invitacion$', views.solicitar_invitacion, name='solicitar invitacion'),
    url(r'encuesta_universidad$', views.encuesta_universidad, name='encuesta universidad'),
    url(r'registro$', views.registro, name='registro'),
    url(r'encuesta_programa$', views.encuesta_programa, name='encuesta programa'),
]
