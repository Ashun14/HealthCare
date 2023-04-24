from django.urls import path
from . import views

app_name = 'health'

urlpatterns = [
    path("", views.healthhome, name="HealthHome"),
    path("healthcategories/", views.healthcategories, name="HealthCategories"),
    path("healthcategories/healthcategorypage/<slug:cat_url>", views.healthcategorypage, name="HealthCategoryPage"),
    path("healthcategories/post/<slug:post_url>", views.healthpost, name="HealthPost"),
]