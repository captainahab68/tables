# Generated by Django 3.1.6 on 2021-02-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210207_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seat',
            field=models.IntegerField(default=0),
        ),
    ]
