from django.shortcuts import render, get_object_or_404
from .models import Film,Rating


def movies(request):
    data = {
        "filmler" : Film.objects.all()
    }
    return render(request,"movies.html",data)


def moviedetails(request, id):
    movie = get_object_or_404(Film, id=id)
    context = { "movie" :movie}
    return render(request,"details.html",context)