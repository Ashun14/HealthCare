from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import os
from django.dispatch import receiver

# Create your models here.

# Insert Different Workouts Categories
class WorkoutCategory(models.Model):
    category_id = models.AutoField
    heading = models.CharField(max_length=40, default='')
    url = models.SlugField(max_length=100, blank=True)
    input_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.heading
    
    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.heading)
        super().save(*args, **kwargs)


def get_image_path(instance, filename):
    return os.path.join('fitness', 'workouts', str(instance.id), filename)


# Insert Multiple Workouts for same Categories
class Workout(models.Model):

# Workout Types
    WORKOUT_TYPES = [
        ('tb', 'Total Body'),
        ('ub', 'Upper Body'),
        ('lb', 'Lower Body'),
        ('cr', 'Core')
    ]

    workouts_id = models.AutoField
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    url = models.SlugField(max_length=100, blank=True)
    workout_time = models.IntegerField(default=10)
    workouts_type = models.CharField(max_length=5, choices=WORKOUT_TYPES, default='tb')
    input_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='fitness/workouts')
    category = models.ForeignKey(WorkoutCategory, on_delete=models.CASCADE, related_name='workouts')

    def __str__(self):
        return self.title
    
    def img_tag(self):
        return format_html('<img src="/media/{}" style="width: 45px; height: 45px; border-radius: 50%;" />'.format(self.img))
    
    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.title)
        super().save(*args, **kwargs)

@receiver(models.signals.pre_delete, sender=Workout)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)

# Show the whole workout in an article form
class WorkoutPost(models.Model):
    post_id = models.AutoField
    title = models.CharField(max_length=200)
    description = RichTextField()
    url = models.SlugField(max_length=100, blank=True)
    author = models.CharField(max_length=100, default='Admin')
    reading_time = models.IntegerField(default=10)
    publish_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(WorkoutCategory, on_delete=models.CASCADE, default='', null=True, related_name= 'category')
    workouts = models.ForeignKey(Workout, on_delete=models.CASCADE, default='', null=True, blank=True,related_name= 'workouts')

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# class Exercise(models.Model):
#     title = models.CharField(max_length=200)
#     url = models.URLField()

#     def __str__(self):
#         return self.title
