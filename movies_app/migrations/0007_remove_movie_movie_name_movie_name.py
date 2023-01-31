# Generated by Django 4.1.5 on 2023-01-31 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0006_actor_movieactor_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_name',
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(db_column='name', db_index=True, default=1, max_length=256),
            preserve_default=False,
        ),
    ]
