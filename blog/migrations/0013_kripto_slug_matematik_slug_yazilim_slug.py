# Generated by Django 4.1.2 on 2022-12-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_contact_mesaj'),
    ]

    operations = [
        migrations.AddField(
            model_name='kripto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='matematik',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='yazilim',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]