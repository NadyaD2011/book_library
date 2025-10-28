from django.shortcuts import render


def show_site(request):
    return render(request, 'movie_list.html')
