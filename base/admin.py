from django.contrib import admin
from .models import Lecture, Notebook, Page, Section, Tag, Topic


admin.site.register(Lecture)
admin.site.register(Notebook)
admin.site.register(Page)
admin.site.register(Section)
admin.site.register(Tag)
admin.site.register(Topic)


