from . import views
from django.urls import path
from django.shortcuts import redirect

urlpatterns = [
    # Travell Website
    path("", views.index, name="index"),
    path("index", lambda request: redirect("/", permanent=True)),
    path("about", views.about, name="about"),
    path("news", views.news, name="news"),
    path("contact", views.contact, name="contact"),
    # Admin Dashboard
    path("admins", views.admins, name="admins"),
]