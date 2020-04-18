from django.urls import path
from .views import storyListing, storyDetail

urlpatterns = [
    path("", storyListing, name="story-listing"),
    path("<slug:slug>", storyDetail, name="story-detail"),
]
