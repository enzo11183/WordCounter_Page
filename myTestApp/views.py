from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import People
import random
random.seed(543)

def truncate(n):
    return int(n * 100) / 100


def index(request):
    people1 = People()
    people1.age = truncate(random.random()*10 %101)
    people1.name = 'degisken1'
    people1.save()

    people2 = People()
    people2.age = truncate(random.random()*10 %101)
    people2.name = 'degisken2'
    people2.save()
    
    peoples = [people1, people2]
    
  
    return render(request, 'index.html', {'peoples': peoples} )

def sonuc(request):
    tempvariable = request.POST['tempvariable']
    result = len(tempvariable.split())
    context = {
        'kelimesayisi' : result
        }
    return render(request, 'second.html', context)

def detay(request):
    
    context = {
        
        }
    return render(request, 'detay.html',context)