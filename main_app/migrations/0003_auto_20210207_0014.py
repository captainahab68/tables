# Generated by Django 3.1.6 on 2021-02-07 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210206_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='dtg',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
