from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Movie


def show_site(request):
    movies = Movie.objects.all()
    user = User.objects.all()[0]

    return render(
        request,
        'movie_list.html',
        {
            'movies': movies,
            'users': user
        }
    )
