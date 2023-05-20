from django.shortcuts import render
from django.http import HttpResponse
from fitness.models import Workout

# Create your views here.
def home(request):
    workouts = Workout.objects.all()[:4]

    card_titles = ['Perfect for Sports-Specific', 'No Equipment Necessary', 'Short on Time?', 'Perfect for Beginners']
    
    context = {
        'workouts': workouts,
        'card_titles': card_titles,
    }

    return render(request, "homepage.html", context)

def termsCondition(request):
    return render(request, "terms_condition.html")

def policy(request):
    return render(request, "policy.html")