# Generated by Django 5.0.2 on 2024-02-18 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]