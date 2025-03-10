from django.urls import path
from .views import bracket_view

urlpatterns = [
    path("bracket/", bracket_view, name="bracket"),
]