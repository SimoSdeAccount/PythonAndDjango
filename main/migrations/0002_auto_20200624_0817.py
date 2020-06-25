# Generated by Django 3.0.7 on 2020-06-24 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorial_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorial_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_published',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
