from django.shortcuts import render, get_object_or_404
from .models import Update, UpdateImage, Contact


def updateListing(request):
    updates = Update.objects.all().order_by("-published_date")
    return render(request, "", {"updates": updates})


def updateDetail(request, slug):
    update = get_object_or_404(Update, slug=slug)
    images = UpdateImage.objects.filter(update=update)
    contacts = Contact.objects.filter(update=update)
    recent = Update.objects.all().order_by("published_date")[:5]
    return render(
        request,
        "",
        {"update": update, "images": images, "contacts": contacts, "recent": recent},
    )
