# Generated by Django 4.1.13 on 2024-05-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0006_remove_film_ımbd_rating_film_rat"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="film",
            name="rat",
        ),
        migrations.AddField(
            model_name="film",
            name="rati",
            field=models.DecimalField(decimal_places=2, default="exit", max_digits=3),
            preserve_default=False,
        ),
    ]
