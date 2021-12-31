from django.shortcuts import render ,get_object_or_404 , redirect
from webapp.models import Persona
from webapp.forms import *

def inicio(request):
    contador = Persona.objects.count()
    registros = Persona.objects.order_by('id')
    mensaje = 'Inicio / SAP'
    return render(request,'inicio.html',{
        'registros' : registros,
        'contador' : contador
    } )

def agregar(request):
    titulo = 'Crear Registro - SAP'
    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else: 
        formulario = PersonaForm()

    return render(request, 'agregar.html' , {
        'titulo' : titulo,
        'formulario' : formulario
    })

def eliminar(request , id):
    registro = get_object_or_404(Persona , pk=id)
    if registro:
        registro.delete()
        return redirect('inicio')

def editar(request , id):
    
    titulo = 'Editar Registro - SAP'
    registro = get_object_or_404(Persona , pk=id)
    if request.method == 'POST':
        formulario = PersonaForm(request.POST , instance= registro)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else: 
        formulario = PersonaForm(instance= registro)

    return render(request, 'editar.html' , {
        'titulo' : titulo,
        'formulario' : formulario
    })

def domicilio(request):
    titulo = 'Agregar Domicilio - SAP'
    if request.method == 'POST':    
        formulario = DomicilioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else: 
        formulario =  DomicilioForm()

    return render(request, 'domicilio.html' , {
        'titulo' : titulo,
        'formulario' : formulario
    })

def detalle(request , id):
    titulo = 'Ver Registro - SAP'
    registro = get_object_or_404(Persona,pk=id)
    return render(request, 'detalle.html' , {
        'titulo' : titulo,
        'registro' : registro
    }) 

