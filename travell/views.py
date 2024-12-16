from .models import destination
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Skydash Website
## Skydash Home Page
def index(request):
    return render(request, "index.html")
## Skydash About Us Page
def about(request):
    return render(request, "about.html")
## Skydash News Page
def news(request):
    return render(request, "news.html")
## Skydash Contact Page
def contact(request):
    return render(request, "contact.html")


# Skydash Admin Side
## Admin Dashboard
def admins(request):
    return render(request, "admin/index.html")
## Admin Add New Admin
def add(request):
    path = ""
    if request.POST:
        title = request.POST.get("title")
        description = request.POST.get("description")
        amount = request.POST.get("amount")

        # Validate form data
        if not title or not description or not amount:
            return render(request, "admin/add.html", {"error": "All fields are required."})

        try:
            amount = int(amount)  # Ensure the amount is an integer
        except ValueError:
            return render(request, "admin/add.html", {"error": "Amount must be a valid number."})

        # Handle file upload
        if len(request.FILES) != 0:
            image = request.FILES["image"]
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            path = fs.url(filename)

            data = {
                "title": title,
                "description": description,
                "amount": amount,
                "image": path
            }
            id = destination.insert_one(data).inserted_id
            print(f"Data Inserted with ID {id}")

            return view(request)  # Ensure 'view' is defined elsewhere
        else:
            return render(request, "admin/add.html", {"error": "Image is required."})
    else:
        return render(request, "admin/add.html", {"error": "Invalid request method."})
## Admin View Admin Details
def view(request):
    data = destination.find()
    context = { "data": data }
    return render(request, "admin/table.html", context)
## Admin Delete Admin Details
def delete(request, title):
    destination.delete_one({ "title": { "$eq": title } })
    return view(request)
## Admin Display Admin Details
def display(request, title):
    data = destination.find_one({ "title": { "$eq": title } })
    context = { "data": data }
    return render(request, "admin/display.html", context)
## Admin Edit Admin Details
def edit(request, title):
    data = destination.find_one({ "title": { "$eq": title } })
    context = { "data": data }
    return render(request, "admin/edit.html", context)