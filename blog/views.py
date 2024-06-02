from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    menu = ['home', 'about', 'posts']
    data = {
        'menu_bar': menu
    }
    return render(request, 'blog/index.html', context=data)

def about(request):
    return render(request, 'blog/about.html')