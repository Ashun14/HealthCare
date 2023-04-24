from django.urls import path
from . import views

app_name = 'nutrition'

urlpatterns = [
    path("", views.nutritionhome, name="NutritionHome"),
    path("nutritioncategories/", views.nutritioncategories, name="NutritionCategories"),
    path("nutritioncategories/nutritioncategorypage/<slug:cat_url>", views.nutritioncategorypage, name="NutritionCategoryPage"),
    path("nutritioncategories/post/<slug:post_url>", views.nutritionpost, name="NutritionPost"),
]