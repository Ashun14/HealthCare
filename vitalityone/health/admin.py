from django.contrib import admin
from health.models import HealthCategory,HealthPost,Tag

# Register your models here.

# Configuration for WorkoutCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'cat_title', 'input_date')
    search_fields = ('cat_title',)
    list_filter = ('sub_cat',)
    list_per_page = 30

# Configuration for Workout

class PostsAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'title', 'author', 'category', 'input_date')
    search_fields = ('title', 'topics', 'author')
    list_filter = ('category', 'author')
    list_per_page = 30

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(HealthCategory, CategoryAdmin)
admin.site.register(HealthPost, PostsAdmin)
admin.site.register(Tag, TagAdmin)
