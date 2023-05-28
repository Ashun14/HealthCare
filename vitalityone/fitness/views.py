from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from fitness.models import Workout, WorkoutCategory,WorkoutPost
from django.core.paginator import Paginator
import random
import requests
from decouple import config
# from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='loginsystem:Login')
def fitnesshome(request):

    categories = WorkoutCategory.objects.all()[:4]

    return render(request, "fitness/fitness_homepage.html", {'categories': categories})

# @login_required(login_url='loginsystem:Login')
def workoutscategories(request):

    categories = WorkoutCategory.objects.all()
    context = {'categories': categories}
    return render(request, "fitness/fitness_workouts_categories.html", context)

# @login_required(login_url='loginsystem:Login')
def workouts(request, url):

    workoutsCatUrl = get_object_or_404(WorkoutCategory, url=url)
    workouts = workoutsCatUrl.workouts.all()
    posts = WorkoutPost.objects.all()

    context = {
        'workoutsCatUrl': workoutsCatUrl, 
        'workouts': workouts,
        'posts': posts,
    }
    return render(request, "fitness/fitness_workouts.html", context)

# @login_required(login_url='loginsystem:Login')
def posts(request, url):

    posts = WorkoutPost.objects.get(url=url)

    workouts = Workout.objects.all()

    nextpost = WorkoutPost.objects.filter(id__gt= posts.id).order_by('id').first()
    prevpost = WorkoutPost.objects.filter(id__lt= posts.id).order_by('id').last()

    # Get the category of the current post
    category = posts.category

    # Find all the posts that belong to the current category, excluding the current post
    related_posts = WorkoutPost.objects.filter(category=category).exclude(id=posts.id)

    # If there are not enough related posts for the current category, find additional related posts from other categories
    
    num_related_posts = 3

    if related_posts.count() > num_related_posts:
        related_posts = related_posts.order_by('-publish_date')[:num_related_posts]
    else:
    # not enough related posts in the same category, so include additional posts from other categories
        remaining_posts = num_related_posts - related_posts.count()
        additional_posts = WorkoutPost.objects.exclude(category=category).order_by('-publish_date')[:remaining_posts]
        related_posts = list(related_posts) + list(additional_posts)
        random.shuffle(related_posts)

    context = {
        'posts': posts,
        'nextpost': nextpost,
        'prevpost': prevpost,
        'related_posts': related_posts,
        'workouts': workouts,
    }
    return render(request, "fitness/fitness_workout_post.html", context)

# @login_required(login_url='loginsystem:Login')
def exercisedatabase(request):
    return render(request, "fitness/fitness_exercisedb.html")
