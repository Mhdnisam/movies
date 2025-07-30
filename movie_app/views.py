from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    movie_details = {'movies':  [{
        'title': 'shidhath',
        'year': 2017,
        'category': 'love story',
        'success': True,
    },
     {
        'title': 'how to train your dragon',
        'year': 2025,
        'category': 'anime movie',
        'success': True,
    },
     {
        'title': 'pulimurugan',
        'year': 2017,
        'category': 'movie',
        'success': True,
    },
     {
        'title': 'bilal',
        'year': 2013,
        'category': 'gangster movie',
        'success': True,
    },
     {
        'title': 'ashique 2',
        'year': 2014,
        'category': 'love story',
        'success': True,
    },
     {
        'title': 'one piece',
        'year': 1995,
        'category': 'anime',
        'success': True,
    }]}
    return render(request, 'hello.html', movie_details)

