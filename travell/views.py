from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def news(request):
    return render(request, "news.html")

def contact(request):
    return render(request, "contact.html")

def admins(request):
    return render(request, "admin/index.html")