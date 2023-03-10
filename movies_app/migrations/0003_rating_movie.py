# Generated by Django 4.1.5 on 2023-01-18 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_rating_remove_movie_description_remove_movie_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='movies_app.movie'),
            preserve_default=False,
        ),
    ]
