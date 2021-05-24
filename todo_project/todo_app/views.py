from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import TodoForm
# Create your views here.
def index(request):
    todos=Todo.objects.all()
    context={
        'todos':todos
    }
    return render(request,'index.html',context)

def addtodo(request):
    form=TodoForm()
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TodoForm(request.POST)
    context={
        'form':form
    }
    return render(request,'add.html',context)

def deletetodo(request,pk):
    todo=Todo.objects.get(id=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('/')
    context={'todo':todo}
    return render(request,'delete.html',context)



