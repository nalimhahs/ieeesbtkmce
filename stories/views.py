from django.shortcuts import render, get_object_or_404
from .models import Story, StoryImage


def storyListing(request):
    stories = Story.objects.all().order_by("-published_date")
    return render(request, "", {"stories": stories})


def storyDetail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    images = StoryImage.objects.filter(story=story)
    recent = Story.objects.all().order_by("published_date")[:5]
    return render(request, "", {"story": story, "images": images, "recent": recent})
