from django.shortcuts import render, redirect 
from .models import Pessoa 

def lista(request): 

    pessoas = Pessoa.objects.all() 
    return render(request, 'lista.html', {'pessoas': pessoas}) 


def nova(request): 

    if request.method == 'POST': 

        Pessoa.objects.create( 

            nome=request.POST['nome'], 

            email=request.POST['email'] 

        ) 

        return redirect('lista') 

    return render(request, 'nova.html') 