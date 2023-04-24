from django.shortcuts import render
from django.http import HttpResponse
from health.models import HealthCategory, HealthPost, Tag
import random
# from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='loginsystem:Login')
def healthhome(request):

    healthcondition = HealthCategory.objects.filter(sub_cat='hc')
    explore = HealthCategory.objects.filter(sub_cat='ex')
    showpost = HealthPost.objects.all()

    top_articles = showpost.order_by('-input_date')[:2]
    top_reads = showpost.exclude(id__in=top_articles).order_by('-views')[:4]
    latest_news = HealthPost.objects.filter(tags__name__icontains='HNews').exclude(id__in=top_articles).exclude(id__in=top_reads).order_by('title')[:4]


    # pass the remaining posts to the template and render them
    context = {
        'healthcondition': healthcondition,
        'explore': explore,
        'showpost': showpost,
        'top_articles': top_articles,
        'top_reads': top_reads,
        'latest_news': latest_news,
     }

    return render(request, "health/health_homepage.html", context)

# @login_required(login_url='loginsystem:Login')

def healthcategories(request):

    categories = HealthCategory.objects.all()

    subcategory = request.GET.get('subcategory')

    if subcategory == 'hc':
        categories = HealthCategory.objects.filter(sub_cat='hc')
    elif subcategory == 'ex':
        categories = HealthCategory.objects.filter(sub_cat='ex')
    else:
        categories = HealthCategory.objects.all()

    posts = HealthPost.objects.all()


    context = {
        'categories': categories,
        'posts': posts,
        }
    return render(request, "health/health_categories.html", context)

# @login_required(login_url='loginsystem:Login')
def healthcategorypage(request, cat_url):

    category = HealthCategory.objects.get(cat_url=cat_url)
    posts = HealthPost.objects.filter(category= category)

    featured_posts = posts.order_by('-input_date')[:2]
    best_in_posts = posts.exclude(id__in=featured_posts).order_by('reading_time')[:4]
    more_in_posts = posts.exclude(id__in=featured_posts).exclude(id__in=best_in_posts).order_by('title')[:6]

    context = {
        'category': category,
        'featured_posts': featured_posts,
        'best_in_posts': best_in_posts,
        'more_in_posts': more_in_posts,
    }

    return render(request, "health/health_category_page.html", context)

def healthpost(request, post_url):

    posts = HealthPost.objects.get(post_url = post_url)

    posts.increase_views() # increase views by 1

    nextpost = HealthPost.objects.filter(id__gt= posts.id).order_by('id').first()
    prevpost = HealthPost.objects.filter(id__lt= posts.id).order_by('id').last()

    category = posts.category

    related_posts_same_category = HealthPost.objects.filter(category=category).exclude(post_url=posts.post_url)
    related_posts_other_categories = HealthPost.objects.exclude(category=category)
    related_posts = list(related_posts_same_category) + list(related_posts_other_categories)
    random.shuffle(related_posts)
    
    context = {
        'posts': posts,
        'nextpost': nextpost,
        'prevpost': prevpost,
        'related_posts':related_posts
    }

    return render(request, "health/health_posts.html", context)