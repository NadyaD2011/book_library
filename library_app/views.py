from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Movie
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import MovieForm
from .models import Genre


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    genres = Genre.objects.all()
    return render(request, 'movie_detail.html', {'movie': movie, 'genres': genres})


def show_site(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    return render(
        request,
        'movie_list.html',
        {
            'movies': movies,
            'genres': genres
        }
    )


def add_movie_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Фильм успешно добавлен!')
            return redirect('/')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})
