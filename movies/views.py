from django.shortcuts import render, get_object_or_404
from .models import Film,Rating
import os, json
from django.http import HttpResponse
from datetime import timedelta


modele_dir = os.path.dirname(__file__)
def add_films(request):
    file_patch = os.path.join(modele_dir,'imdb_top_films.json')
    with open(file_patch, "r",encoding="utf-8") as f:
        data = json.load(f)
    no_added = 0
    for film in data:
        dur = film["Runtime"]
        f_dur = timedelta(minutes=int(dur[0:-4]))
        obj = Film.objects.update_or_create(
            title = film["Series_Title"],
            released = f"{film['Released_Year']}-01-01",
            certificate = film["Certificate"],
            duration = f_dur,
            genre = film["Genre"],
            director = film["Director"],
            star1 = film["Star1"],
            star2 = film["Star2"],
            star3 = film["Star3"],
            star4 = film["Star4"],
            overview = film["Overview"],
            poster = film["Poster_Link"],
        )
        no_added += 1
    msg = f"Added {no_added} films to the database."
    return HttpResponse(msg,content_type="text/plain")







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