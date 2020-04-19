from django.shortcuts import render
from .models import Section


def aboutPage(request):
    sections = Section.objects.all()
    return render(request, "about/about.html", {"sections": sections})
