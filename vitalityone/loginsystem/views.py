from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


from django.contrib import messages

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' +  user)


                return redirect('loginsystem:Login')


        context = {'form': form}
        return render(request, 'loginsystem/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request, 'Username OR Password is incorrect')
            
        context = {}
        return render(request, 'loginsystem/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginsystem:Login')