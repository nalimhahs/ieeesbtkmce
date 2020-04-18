from django.urls import path
from .views import updateListing, updateDetail

urlpatterns = [
    path("", updateListing, name="update-listing"),
    path("<slug:slug>", updateDetail, name="update-detail"),
]
