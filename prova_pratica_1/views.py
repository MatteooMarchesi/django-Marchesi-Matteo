from django.shortcuts import render
from .models import Materia
from django.http import JsonResponse 

def view_b(request):
    context={
        'materie' :['Matematica','Italiano','Inglese','Storia','Geografia']
    }
    return render(request,"view_b.html",context)

def view_c(request):
    context={
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
                  'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
                  'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]}
    }
    return render (request,"view_c.html",context)

def view_d(request):
    materie=Materia.objects.all()
    context={"materie": materie}
    return render(request, "view_d.html",context)


def viewAPI(request):
    context={
        'materie' :['Matematica','Italiano','Inglese','Storia','Geografia']
    }
    response = JsonResponse(context)
    return response
