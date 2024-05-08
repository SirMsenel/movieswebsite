from django.shortcuts import render, get_object_or_404
from .models import Film,Rating


def movies(request):
    data = {
        "filmler" : Film.objects.all()
    }
    return render(request,"movies.html",data)


def moviedetails(request, id):
    movie = get_object_or_404(Film, id=id)
    total_second = int(movie.duration.total_seconds())
    hours = total_second//3600
    minutes = (total_second % 3600) // 60
    duration = f"{hours}h {minutes}m" 


    context = { "movie" :movie,"dura":duration}
    return render(request,"details.html",context)