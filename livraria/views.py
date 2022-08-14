from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import livro
from .forms import livroForm
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
def osoutros(request):
    return render(request,'paginas/osoutros.html')

def livros(request):
    livros = livro.objects.all()
    return render(request, 'livros/index.html',{'livros':livros})
def criarLivro(request):
    formulario = livroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('livros')
        
        
    return render(request, 'livros/criar.html', {'formulario': formulario})
def editarLivro(request,id):
    lv= livro.objects.get(id=id)
    formulario = livroForm(request.POST or None, request.FILES or None, instance=lv)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('livros')
        
    return render(request, 'livros/editar.html', {'formulario': formulario})
    
def eliminar(request,id):
    lv= livro.objects.get(id=id)
    lv.delete()
    return redirect('livros')
    
