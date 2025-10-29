from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Movie
from django.shortcuts import get_object_or_404


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})


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
