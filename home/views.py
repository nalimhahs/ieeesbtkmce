from django.shortcuts import render
from .models import Carousel, Awards, Society
from updates.models import Update
from stories.models import Story


def homePage(request):
    carousel = Carousel.objects.all()
    awards = Awards.objects.all()
    updates = Update.objects.all()[:3]
    stories = Story.objects.all()[:3]
    societies = Society.objects.all()

    return render(
        request,
        "home/home.html",
        {
            "carousel": carousel,
            "awards": awards,
            "updates": updates,
            "stories": stories,
            "societies": societies,
        },
    )

