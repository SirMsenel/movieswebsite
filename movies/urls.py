from django.urls import path
from . import views


urlpatterns = [
    path("", views.movies, name="movies"),
    path("movies", views.movies, name="movies"),
    path("movies/<int:id>", views.moviedetails, name="details"),
    path("add_films",views.add_films,name="add_films"),
    path("add_reviews", views.add_reviews, name="add_reviews")
    
]