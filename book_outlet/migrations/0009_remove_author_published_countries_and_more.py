# Generated by Django 4.1 on 2022-09-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0008_alter_author_published_countries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='published_countries',
        ),
        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(related_name='books', to='book_outlet.country'),
        ),
    ]
