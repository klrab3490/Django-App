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
    path("admins", views.admins, name="admins"),                        # Admin listing or management
    path("add", views.add, name="add"),                                 # Add new admin
    path("view", views.view, name="view"),                              # Table View Of Database Data
    path("delete?id=<str:title>", views.delete, name="delete"),         # Delete Admin Details
    path("display?id=<str:title>", views.display, name="display"),      # Display Admin Details
    path("edit?id=<str:title>", views.edit, name="edit"),               # Edit Admin Details
]
