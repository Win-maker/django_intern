from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     pass
#
def login(request):
    return render(request,'login.html')

def sendData(request):
    name = request.POST['username']
    password = request.POST['password']
    return render(request, 'info_details.html', {'name':name, 'email':password})