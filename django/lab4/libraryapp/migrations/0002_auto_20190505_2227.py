# Generated by Django 2.0 on 2019-05-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_name',
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.ManyToManyField(to='libraryapp.Author'),
        ),
    ]
