# Generated by Django 3.2.19 on 2023-05-04 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='content',
        ),
    ]
