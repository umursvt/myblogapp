# Generated by Django 4.1.2 on 2022-11-21 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_blog_kripto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kripto',
            name='guncelleme_tarih',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='kripto',
            name='tarih',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
