from multiprocessing import context
import re
from django.shortcuts import render
from main.models import About, Category, Home, Portfolio, Profile, Skills

# Create your views here.
def index(request):
    #Home
    home = Home.objects.latest('update')

    #About
    about = About.objects.latest('update')
    profiles = Profile.objects.filter(about = about)

    #Skills
    categories = Category.objects.all()

    #Portfolio
    portfolios = Portfolio.objects.all()




    context ={
        'home' : home,
        'about': about,
        'profile': profiles,
        'categories': categories,
        'portfolios': portfolios
    }
    return render(request, 'index.html', context)
