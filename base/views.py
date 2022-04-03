from django.shortcuts import render
from .models import Lecture, Notebook, Page, Section, Tag, Topic
from django.db.models.query_utils import Q


def home(request):
    query = ''
    # request_form = request.dict()

    all_notebooks = Notebook.objects.all()
    all_lectures = Lecture.objects.all()

    notebooks = all_notebooks.filter(
        Q(tags__name__icontains=query)
    ).distinct()

    context = {"notebooks": notebooks, "all_lectures": all_lectures}
    return render(request, 'base/homepage/main.html', context)
