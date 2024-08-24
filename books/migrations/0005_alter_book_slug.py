# Generated by Django 5.1 on 2024-08-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='', max_length=250, unique_for_date='published_date'),
        ),
    ]
