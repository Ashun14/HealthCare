from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import os

# Create your models here.

class NutritionQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for post in self:
            post.delete()
        super().delete(*args, **kwargs)

class Tag(models.Model):
    TAG_SECTION = [
        ('NNews', 'News'),
        ('NTips', 'Tips & Tricks'),
    ]
    name = models.CharField(max_length=10, choices=TAG_SECTION, blank=True)

    def __str__(self):
        return self.name

# Nutrition Categories

class NutritionCategory(models.Model):

    CAT_SECTION = [
        ('ex', 'Explore'),
        ('lh', 'Living Healthy')
    ]

    category_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')
    img = models.ImageField(upload_to='nutrition/categories')
    sub_cat = models.CharField(max_length=2, choices=CAT_SECTION, default='ex')
    cat_url = models.SlugField(max_length=100, blank= True)
    input_date = models.DateTimeField(default=timezone.now)

    objects = NutritionQuerySet.as_manager()

    def __str__(self):
        return self.cat_title

    def img_tag(self):
        return format_html('<img src="/media/{}" style="width: 45px; height: 45px; border-radius: 50%;" />'.format(self.img))
    
    def save(self, *args, **kwargs):
        if not self.cat_url:
            self.cat_url = slugify(self.cat_title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(self.img.path)
        super().delete(*args, **kwargs)

# Nutrition Post based on Categories

class NutritionPost(models.Model):

    post_id = models.AutoField
    title = models.CharField(max_length=200)
    sub_description = models.CharField(max_length=200)
    description = RichTextField()
    author = models.CharField(max_length=100, default='Admin')
    post_url = models.SlugField(max_length=200, blank= True)
    img = models.ImageField(upload_to='nutrition/posts')
    input_date = models.DateField(default=timezone.now)
    reading_time = models.IntegerField(default=10)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(NutritionCategory, on_delete=models.CASCADE, related_name='category')
    views = models.PositiveIntegerField(default=0)

    objects = NutritionQuerySet.as_manager()

    def __str__(self):
        return self.title
    
    def img_tag(self):
        return format_html('<img src="/media/{}" style="width: 45px; height: 45px; border-radius: 50%;" />'.format(self.img))
    
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    
    def save(self, *args, **kwargs):
        if not self.post_url:
            self.post_url = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(self.img.path)
        super().delete(*args, **kwargs)