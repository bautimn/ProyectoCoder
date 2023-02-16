from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario

# from AppCoder.models import Curso

def inicio(request):
    return render(request, 'appcoder/inicio.html')

def cursos(request):
    mis_cursos = Curso.objects.all()

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(Nombre=informacion['curso'], camada=informacion['camada'])
            curso.save

            nuevo_curso = {'nombre': informacion['curso'], 'camada': informacion['camada']}
            return render(request, 'appcoder/cursos.html', {'formulario_curso': mi_formulario,
                                                           'nuevo_curso': nuevo_curso,
                                                            'mis_cursos': mis_cursos})
        else:
            mi_formulario = CursoFormulario()

        return render(request, 'appcoder/cursos.html', {'formulario_curso': mi_formulario, 
                                                        'mis_cursos': mis_cursos})
                
def profesores(request):
    return render(request, 'appcoder/profesores.html')

def estudiantes(request):
    return render(request, 'appcoder/estudiantes.html')

def entregables(request):
    return render(request, 'appcoder/entregables.html')

def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            nuevo_curso.save()
            return redirect('inicio')

    mi_formulario = CursoFormulario()
    return render(request, 'appcoder/curso-formulario.html', {'formulario_curso': mi_formulario})

def profesor_formulario(request):

    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], 
                                    apellido=informacion['apellido'], 
                                    email=informacion['email'], 
                                    profesion=informacion['profesion'])
            profesor.save()
            return redirect('inicio')
    else:
        mi_formulario = ProfesorFormulario()
        return render(request, 'appcoder/profesor-formulario.html', {'formulario_profesor': mi_formulario})

def buscar_camada(request):

    return render(request, 'appcoder/busqueda-camada.html')

def buscar(request):
    
    if request.GET['camada']:
        mi_camada = request.GET['camada']
        resultado = Curso.objects.filter(camada__icontains=mi_camada)

        return render(request, 'appcoder/resultados-busqueda.html', {'cursos': resultado, 'camada': mi_camada})

    else:
        respuesta = 'No se encontro esa camada'
    return HttpResponse(respuesta)