from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

cities = ['yangon', 'mandalay', 'bagan', 'pyinoolwin','taunggyi','mawlamyaing']


def home(request):
    return render(request, 'weather_home.html')

def add(request):
    answer = request.POST['city']
    if answer in cities:
        return render(request, 'weather.html', {'answer':answer})


