from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index (request):
    return render(request,'recipes/index.html',context={
        "name":"vinicius"
    })


def contato (request):
    return render(request,'recipes/CONTATO')

def sobre(request):
    return HttpResponse('recipes/sobre')