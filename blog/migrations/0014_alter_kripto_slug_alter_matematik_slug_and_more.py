# Generated by Django 4.1.2 on 2022-12-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_kripto_slug_matematik_slug_yazilim_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kripto',
            name='slug',
            field=models.SlugField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='matematik',
            name='slug',
            field=models.SlugField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='yazilim',
            name='slug',
            field=models.SlugField(blank=True, default=' '),
        ),
    ]
