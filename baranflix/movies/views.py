from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    movies = Movie.objects.all
    form = MovieForm()
    
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'movies': movies, 'form': form,}
    return render(request, "movies/list.html", context)

def updateMovie(request, pk):
    movie = Movie.objects.get(id = pk)
    
    form = MovieForm(instance = movie)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'form': form}
    
    return render(request, 'movies/update_movie.html', context)

def deleteMovie(request, pk):
    item = Movie.objects.get(id = pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item': item}
    return render(request, 'movies/delete.html', context)