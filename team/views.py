from django.shortcuts import render
from .models import Team


def listTeam(request):

    teams = Team.objects.all().order_by("start")
    return render(request, "", {"teams": teams})
