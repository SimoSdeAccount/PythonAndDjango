# Generated by Django 3.0.7 on 2020-06-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200624_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='slug',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
