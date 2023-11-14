from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import updated
from .models import film


# Create your views here.
def home(request):
    movie=film.objects.all()
    context={
        'films':movie
    }
    return render(request,'index.html',context)
def details(request,movieid):
    films=film.objects.get(id=movieid)
    return render(request,'details.html',{'id':films})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year', )
        img=request.FILES['img']
        films=film(name=name,desc=desc,year=year,img=img)
        films.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie=film.objects.get(id=id)
    form=updated(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=film.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
