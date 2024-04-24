from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("kazeem", views.kazeem, name="kazeem"),
    path("fortune", views.fortune, name="fortune"),
]
