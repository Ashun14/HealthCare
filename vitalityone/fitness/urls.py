from django.urls import path
from . import views

app_name = 'fitness'

urlpatterns = [
    path("", views.fitnesshome, name="FitnessHome"),
    path("exercisedatabase/", views.exercisedatabase, name="ExerciseDb"),
    path("workoutscategories/", views.workoutscategories, name="WorkoutsCategories"),
    path("workoutscategories/workouts/<slug:url>", views.workouts, name="Workouts"),
    path("workoutscategories/workouts/posts/<slug:url>", views.posts, name="Posts"),
]