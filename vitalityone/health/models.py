import math
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import os
from PIL import Image

# Create your models here.

class HealthQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for post in self:
            post.delete()
        super().delete(*args, **kwargs)

class Tag(models.Model):
    TAG_SECTION = [
        ('HNews', 'News'),
        ('HTips', 'Tips & Tricks'),
    ]
    name = models.CharField(max_length=10, choices=TAG_SECTION, blank=True)

    def __str__(self):
        return self.name

# Health Categories

class HealthCategory(models.Model):

    CAT_SECTION = [
        ('ex', 'Explore'),
        ('hc', 'HealthCondition')
    ]

    category_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')
    img = models.ImageField(upload_to='health/categories')
    sub_cat = models.CharField(max_length=2, choices=CAT_SECTION, default='ex')
    cat_url = models.SlugField(max_length=100, blank= True)
    input_date = models.DateTimeField(default=timezone.now)

    objects = HealthQuerySet.as_manager()

    def __str__(self):
        return self.cat_title

    def img_tag(self):
        return format_html('<img src="/media/{}" style="width: 45px; height: 45px; border-radius: 50%;" />'.format(self.img))
    
    def save(self, *args, **kwargs):
        if not self.cat_url:
            self.cat_url = slugify(self.cat_title)

        if self.pk is not None:  # object has already been saved to db
            old_self = HealthCategory.objects.get(pk=self.pk)
            if old_self.img != self.img:  # img field has changed
                if os.path.exists(old_self.img.path):
                    os.remove(old_self.img.path)
        
        super().save(*args, **kwargs)

        if self.img:
            if os.path.exists(self.img.path):
                img = Image.open(self.img.path)
                max_size = (800, 800)
                img.thumbnail(max_size)
                img.save(self.img.path, format='JPEG', optimize=True, quality=80)

    def delete(self, *args, **kwargs):
        if self.img and os.path.exists(self.img.path):
            os.remove(self.img.path)
        super().delete(*args, **kwargs)

# Health Post based on Categories

class HealthPost(models.Model):

    post_id = models.AutoField
    title = models.CharField(max_length=200)
    sub_description = models.CharField(max_length=200)
    description = RichTextField()
    author = models.CharField(max_length=100, default='Admin')
    post_url = models.SlugField(max_length=200, blank= True)
    img = models.ImageField(upload_to='health/posts')
    input_date = models.DateField(default=timezone.now)
    reading_time = models.IntegerField(default=10)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(HealthCategory, on_delete=models.CASCADE, related_name='category')
    views = models.PositiveIntegerField(default=0)

    objects = HealthQuerySet.as_manager()

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
        
        if self.pk is not None:  # object has already been saved to db
            old_self = HealthPost.objects.get(pk=self.pk)
            if old_self.img != self.img:  # img field has changed
                if os.path.exists(old_self.img.path):
                    os.remove(old_self.img.path)
        
        words_per_minute =  183
        word_count = len(self.description.split())
        self.reading_time = math.ceil(word_count / words_per_minute)
        super().save(*args, **kwargs)

        if self.img:
            if os.path.exists(self.img.path):
                img = Image.open(self.img.path)
                max_size = (1280, 720)
                img.thumbnail(max_size)
                img.save(self.img.path, format='JPEG', optimize=True, quality= 80)

    def delete(self, *args, **kwargs):
        if self.img and os.path.exists(self.img.path):
            os.remove(self.img.path)
        super().delete(*args, **kwargs)