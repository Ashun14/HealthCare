# Generated by Django 4.2 on 2023-04-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_tag_nutritionpost_views_remove_nutritionpost_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionpost',
            name='tags',
            field=models.ManyToManyField(blank=True, to='nutrition.tag'),
        ),
    ]
