import random
from django.shortcuts import render
from django.http import HttpResponse
from fitness.models import Workout, WorkoutCategory

# Create your views here.
def home(request):
    workouts = []
    category_set = set()

    while len(workouts) < 4:
        workout = random.choice(Workout.objects.all())
        category = workout.category

        if category not in category_set:
            workouts.append(workout)
            category_set.add(category)
    
    context = {
        'workouts': workouts,
    }

    return render(request, "homepage.html", context)

def termsCondition(request):
    return render(request, "terms_condition.html")

def policy(request):
    return render(request, "policy.html")