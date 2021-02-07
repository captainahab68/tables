# Generated by Django 3.1.6 on 2021-02-07 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210207_0133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cover',
            new_name='Order',
        ),
        migrations.RemoveField(
            model_name='table',
            name='covers',
        ),
        migrations.AddField(
            model_name='table',
            name='orders',
            field=models.ManyToManyField(to='main_app.Order'),
        ),
    ]