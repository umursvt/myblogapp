# Generated by Django 4.1.2 on 2022-12-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_kripto_aciklama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mesaj',
            field=models.TextField(max_length=350),
        ),
    ]