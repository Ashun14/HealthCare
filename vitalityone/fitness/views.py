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
    url = "https://wger.de/api/v2/exercise/"
    api_key = config('API_KEY')
    headers = {
        "Authorization": f"Token {api_key}",  # Replace YOUR_API_KEY with your wger.de API key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        exercises = data['results']
    else:
        exercises = []

    context = {
        'api_key': api_key,
        'exercises': exercises,
        'bodyparts': get_bodyparts(),
        'muscles': get_muscles(),
        'equipments': get_equipments(),
    }
    return render(request, "fitness/fitness_exercisedb.html", context)

def exercise_search(request):
    url = "https://wger.de/api/v2/exercise/"
    headers = {
        "Authorization": f"Token {config('API_KEY')}",  # Replace YOUR_API_KEY with your wger.de API key
    }
    params = {
        'language': 2,  # Language code for English
    }

    bodypart_id = request.GET.get('bodypart')
    muscle_id = request.GET.get('muscle')
    equipment_id = request.GET.get('equipment')
    search_query = request.GET.get('search_query')

    if bodypart_id:
        params['category'] = bodypart_id
    if muscle_id:
        params['muscles'] = muscle_id
    if equipment_id:
        params['equipment'] = equipment_id
    if search_query:
        params['name'] = search_query

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        exercises = data['results']
    else:
        exercises = []

    paginator = Paginator(exercises, 10)  # Show 10 exercises per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'exercises': page_obj,
        'bodyparts': get_bodyparts(),  # Replace with the function to fetch bodyparts
        'muscles': get_muscles(),  # Replace with the function to fetch muscles
        'equipments': get_equipments(),  # Replace with the function to fetch equipments
        'search_query': search_query,
    }
    return render(request, 'fitness/fitness_exercisedb.html', context)

def get_bodyparts():
    url = "https://wger.de/api/v2/exercisecategory/"
    headers = {
        "Authorization": f"Token {config('API_KEY')}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        bodyparts = data['results']
    else:
        bodyparts = []
    return bodyparts

def get_muscles():
    url = "https://wger.de/api/v2/muscle/"
    headers = {
        "Authorization": f"Token {config('API_KEY')}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        muscles = data['results']
    else:
        muscles = []
    return muscles

def get_equipments():
    url = "https://wger.de/api/v2/equipment/"
    headers = {
        "Authorization": f"Token {config('API_KEY')}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        equipments = data['results']
    else:
        equipments = []
    return equipments
