# Generated by Django 4.1 on 2022-08-12 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_profile_description_profile_howto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
        migrations.AddField(
            model_name='profile',
            name='com',
            field=models.TextField(default='SOME STRING', max_length=250),
        ),
    ]