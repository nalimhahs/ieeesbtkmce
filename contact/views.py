from django.shortcuts import render
from .forms import ContactForm


def contactPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            # contact.published_date = timezone.now()
            contact.save()
    else:
        form = ContactForm()
    return render(request, "", {"form": form})
