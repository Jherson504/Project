from django.shortcuts import render



def home(request):
    return render(request, 'base/homepage/main.html')
