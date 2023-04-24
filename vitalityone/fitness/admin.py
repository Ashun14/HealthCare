from django.contrib import admin
from fitness.models import WorkoutCategory,Workout,WorkoutPost

# Register your models here.

# Configuration for WorkoutCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('heading', 'input_date')
    search_fields = ('heading',)
    list_per_page = 30

# Configuration for Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'title', 'workouts_type', 'category', 'input_date')
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 30


admin.site.register(WorkoutCategory, CategoryAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutPost)
