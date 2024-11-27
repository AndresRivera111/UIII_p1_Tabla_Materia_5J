from django.shortcuts import render, redirect
from .models import Juguetes

# Create your views here.
def inicio_vistaJuguetes (request):
    lista = Juguetes.objects.all()
    return render(request, 'gestionarJuguetes.html', {'misjuguetes' : lista})

def registrarJuguetes(request):
    id=request.POST['txtid']
    nombre=request.POST['txtnombre']
    marca=request.POST['txtmarca']
    precio=request.POST['txtprecio']
    proveedor=request.POST['txtproveedor']
    clasificacion=request.POST['txtclasificacion']

    guardarJuguetes=Juguetes.objects.create(
    id=id, nombre=nombre, marca=marca)
    return redirect("/")

""" def seleccionarMateria(request, codigo):
    materia = Materia.objects.get(codigo=codigo)
    return render(request,'editarmateria.html', {'mismaterias': materia})

def editarMateria(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['numcreditos']
    materia = Materia.objects.get(codigo=codigo)
    materia.nombre = nombre
    materia.creditos = creditos
    materia.save() # guarda registro actualizado
    return redirect("/")

def borrarMateria(request, codigo):
    materia = Materia.objects.get(codigo=codigo)
    materia.delete() # borra el registro
    return redirect("/") """