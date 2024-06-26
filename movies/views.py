from django.shortcuts import render,redirect, get_object_or_404
from .models import Film,Rating
from django.db.models import Avg
import os, json
from django.http import HttpResponse
from datetime import timedelta
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from random import randint

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



def add_rev(g_film, g_user, g_rating):
    obj = Rating.objects.update_or_create(
        film = get_object_or_404(Film, pk=g_film),
        user = get_object_or_404(User,pk= g_user),
        rating = g_rating,
    )



def movies(request):
    films = Film.objects.all()
    paginator = Paginator(films, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"filmler" : films, "page_obj" : page_obj}
    return render(request,"movies.html",context)




def moviedetails(request, id):
    movie = get_object_or_404(Film, id=id)
    total_second = int(movie.duration.total_seconds())
    hours = total_second//3600
    minutes = (total_second % 3600) // 60
    duration = f"{hours}h {minutes}m" 
    genres = movie.genre.split(",")

    context = { "movie" :movie,"dura":duration,"genres":genres}
    return render(request,"details.html",context)


def add_reviews(request):
    for j in range(0,10000):
        for i in range(1,5):
            filmID = randint(1,692)
            filmRating = randint(1,10)
            add_rev(filmID,i,filmRating)
    return redirect("/movies")