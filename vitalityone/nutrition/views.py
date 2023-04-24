from django.shortcuts import render
from django.http import HttpResponse
from nutrition.models import NutritionCategory, NutritionPost, Tag
import random
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='loginsystem:Login')
def nutritionhome(request):

    livinghealthy = NutritionCategory.objects.filter(sub_cat='lh')
    explore = NutritionCategory.objects.filter(sub_cat='ex')
    showpost = NutritionPost.objects.all()

    top_articles = showpost.order_by('-input_date')[:2]
    top_reads = showpost.exclude(id__in=top_articles).order_by('-views')[:4]
    latest_news = NutritionPost.objects.filter(tags__name__icontains='NNews').exclude(id__in=top_articles).exclude(id__in=top_reads).order_by('title')[:4]

    # pass the remaining posts to the template and render them
    context = {
        'livinghealthy': livinghealthy,
        'explore': explore,
        'showpost': showpost,
        'top_articles': top_articles,
        'top_reads': top_reads,
        'latest_news': latest_news,
     }

    return render(request, "nutrition/nutrition_homepage.html", context)

# @login_required(login_url='loginsystem:Login')

def nutritioncategories(request):

    categories = NutritionCategory.objects.all()

    subcategory = request.GET.get('subcategory')

    if subcategory == 'lh':
        categories = NutritionCategory.objects.filter(sub_cat='lh')
    elif subcategory == 'ex':
        categories = NutritionCategory.objects.filter(sub_cat='ex')
    else:
        categories = NutritionCategory.objects.all()


    context = {'categories': categories}
    return render(request, "nutrition/nutrition_categories.html", context)

# @login_required(login_url='loginsystem:Login')
def nutritioncategorypage(request, cat_url):

    category = NutritionCategory.objects.get(cat_url=cat_url)
    posts = NutritionPost.objects.filter(category= category)

    featured_posts = posts.order_by('-input_date')[:2]
    best_in_posts = posts.exclude(id__in=featured_posts).order_by('reading_time')[:4]
    more_in_posts = posts.exclude(id__in=featured_posts).exclude(id__in=best_in_posts).order_by('title')[:6]

    context = {
        'category': category,
        'featured_posts': featured_posts,
        'best_in_posts': best_in_posts,
        'more_in_posts': more_in_posts,
    }

    return render(request, "nutrition/nutrition_category_page.html", context)

def nutritionpost(request, post_url):

    posts = NutritionPost.objects.get(post_url = post_url)

    posts.increase_views() # increase views by 1

    nextpost = NutritionPost.objects.filter(id__gt= posts.id).order_by('id').first()
    prevpost = NutritionPost.objects.filter(id__lt= posts.id).order_by('id').last()

    category = posts.category

    related_posts_same_category = NutritionPost.objects.filter(category=category).exclude(post_url=posts.post_url)
    related_posts_other_categories = NutritionPost.objects.exclude(category=category)
    related_posts = list(related_posts_same_category) + list(related_posts_other_categories)
    random.shuffle(related_posts)
    
    context = {
        'posts': posts,
        'nextpost': nextpost,
        'prevpost': prevpost,
        'related_posts':related_posts
    }
    
    context = {
        'posts': posts,
    }

    return render(request, "nutrition/nutrition_posts.html", context)