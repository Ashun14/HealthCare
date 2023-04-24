from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact

# Create your views here.
def about(request):
    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        message= request.POST['message']

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return render(request, "about/about.html", {'name' : name})
    else:
        return render(request, "about/about.html", {})