# Generated by Django 3.2.7 on 2021-10-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextended',
            name='is_coach',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userextended',
            name='is_dietician',
            field=models.BooleanField(default=False),
        ),
    ]