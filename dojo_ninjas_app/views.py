from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    all_dojos = Dojo.objects.all()
    all_ninjas = Ninja.objects.all
    context={
        'all_dojos': all_dojos,
        'all_ninjas': all_ninjas
    }
    return render(request, 'index.html', context)


def process_dojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(name = name, city=city, state = state)
    return redirect('/')


def process_ninja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo = request.POST['dojo']
    dojo_obj = Dojo.objects.get(name = dojo)

    Ninja.objects.create( first_name = first_name, last_name=last_name, dojo = dojo_obj)
    return redirect('/')

def delete(request):
    dojo_id = request.POST['delete']
    Dojo.objects.get(id=dojo_id).delete()

    return redirect('/')

