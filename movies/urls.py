from django.urls import path
from . import views


urlpatterns = [
    path("", views.movies, name="movies"),
    path("movies", views.movies, name="movies"),
    path("movies/<int:id>", views.moviedetails, name="details"),
    
]