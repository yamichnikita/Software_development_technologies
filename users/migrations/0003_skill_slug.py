# Generated by Django 4.0.6 on 2022-07-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_social_github_profile_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='slug',
            field=models.SlugField(default='name'),
        ),
    ]
