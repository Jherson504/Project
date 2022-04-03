from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ['-created', 'name']


class Topic(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ['-created', 'name']


class Notebook(models.Model):
    tags = models.ManyToManyField(Tag, blank=True,  related_name='notebooks')
    topics = models.ManyToManyField(
        Topic, blank=True,  related_name='notebooks')
    name = models.CharField(max_length=200)
    description = models.TextField(default="No Description")
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ['-created', 'name']


class Lecture(models.Model):
    notebook = models.ForeignKey(
        Notebook, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True,  related_name='lectures')
    topics = models.ManyToManyField(
        Topic, blank=True,  related_name='lectures')
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ['-created', 'title']


class Page(models.Model):
    notebook = models.ForeignKey(
        Notebook, null=True, related_name='pages', on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return str(super(models.Model, self).sections.title)


class Section(models.Model):
    page = models.ForeignKey(
        Page, related_name='sections', blank=True, null=True, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True,  related_name='sections')
    topics = models.ManyToManyField(
        Topic, blank=True,  related_name='sections')
    title = models.CharField(max_length=200)

    body = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ['-created', 'title']
