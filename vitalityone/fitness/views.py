from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from fitness.models import Workout, WorkoutCategory,WorkoutPost
from django.core.paginator import Paginator
import random
# from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='loginsystem:Login')
def fitnesshome(request):

    categories = WorkoutCategory.objects.all()[:4]

    return render(request, "fitness/fitness_homepage.html", {'categories': categories})

# @login_required(login_url='loginsystem:Login')
def exercisedatabase(request):
    return render(request, "fitness/fitness_exercisedb.html")

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
    if len(related_posts) < num_related_posts:
        num_missing_posts = num_related_posts - len(related_posts)
        missing_posts = WorkoutPost.objects.exclude(id=posts.id).exclude(category=category)[:num_missing_posts]
        related_posts = related_posts.union(missing_posts)
        random.shuffle(related_posts)

    context = {
        'posts': posts,
        'nextpost': nextpost,
        'prevpost': prevpost,
        'related_posts': related_posts,
        'workouts': workouts,
    }
    return render(request, "fitness/fitness_workout_post.html", context)
