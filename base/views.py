from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from .models import Lecture, Notebook, Page, Section, Tag, Topic
from django.db.models.query_utils import Q
from django.contrib import messages


def authenticate_user(request):
    if request.user.is_authenticated:
        return redirect('logout-user')
    return redirect('login-user')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home-page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(username, password, user)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'base/auth/login.html')

    return render(request, 'base/auth/login.html')


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('home-page')

    if request.method == 'GET':
        if request.GET.get('confirm'):
            logout(request)
            return redirect('home')

    return render(request, 'base/auth/logout.html')


def sign_up_user(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    return render(request, 'base/auth/sign-up.html')


def home(request):
    query = ''
    # request_form = request.dict()

    all_notebooks = Notebook.objects.all()
    all_lectures = Lecture.objects.all()
    all_topics = Topic.objects.all()
    all_tags = Tag.objects.all()

    notebooks = all_notebooks.filter(
        Q(tags__name__icontains=query)
    ).distinct()

    context = {"tags": all_tags, "topics": all_topics, "notebooks": notebooks,
               "all_lectures": all_lectures}
    return render(request, 'base/homepage/main.html', context)
