# Generated by Django 5.0 on 2024-01-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_directors'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_info',
            name='poster',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
