from django.shortcuts import render
from django.http import HttpResponse

from cliente.forms import UserForm
from .forms import ProfileForm

def index(request):
    return HttpResponse("Frontend cliente :D")


def invitaciones(request):
    return render(request, 'invitaciones.html', {})


def crear_encuesta(request):
    return render(request, 'crear_encuesta.html', {})


def config(request):
    return render(request, 'config.html', {})


def informacion_curso(request):
    return render(request, 'encuesta_curso_info_1.html', {})


def admin_home(request):
    return render(request, 'home_admin.html', {})


def encuesta(request):
    return render(request, 'encuesta_curso_curriculum.html', {})


def solicitar_invitacion(request):
    return render(request, 'solicitar_invitacion.html', {})


def encuesta_universidad(request):
    return render(request, 'encuesta_universidad.html', {})


def registro(request): # TODO método dummy
    user_form = UserForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        pass
    else:
        pass

    return render(request, 'registro.html', {'user_form': user_form,
                                             'profile_form' : profile_form
                                             })


def encuesta_programa(request):
    return render(request, 'encuesta_programa.html', {})
