from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import numpy as np

def home(request):
    return render(request,'passgen/home.html')

def Password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upper'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('nums'):
        characters.extend(list('0123456789'))
    if request.GET.get('specs'):
        characters.extend(list('!@#$%^&*()_+"<>'))

    length = int(request.GET.get('length',11))
    thepass = ''
    for i in range(length):
        x = np.random.randint(0,len(characters))
        thepass += characters[x]

    return render(request,'passgen/password.html', {'password': thepass})

def about(request):
    return render(request,'passgen/about.html')
