from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Curso,Grado
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def degree(request):
    curso = Curso.objects.all()
    context ={
        'curso': curso
    }
    return render(request, 'core/products.html',context)

def exit(request):
    logout(request)
    return redirect('home')
