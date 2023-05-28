from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Contact

def about(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Invalid email address.')
            return render(request, "about/about.html")

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return render(request, "about/about.html", {'success_message': f'Thanks {name}.'})
    else:
        return render(request, "about/about.html")
