from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')

def add(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    address = request.POST['address']
    return render(request, 'result.html', {'name':name, 'email':email, 'password':password, 'address':address} )