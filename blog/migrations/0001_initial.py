# Generated by Django 4.1.2 on 2022-11-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50)),
                ('resim', models.ImageField(upload_to='media')),
                ('aciklama', models.TextField(max_length=200)),
                ('yazar', models.CharField(max_length=25)),
                ('tarih', models.DateField(auto_now_add=True)),
                ('guncelleme_tarih', models.DateField(auto_now=True)),
            ],
        ),
    ]
