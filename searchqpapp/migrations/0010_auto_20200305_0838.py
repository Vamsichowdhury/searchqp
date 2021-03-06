# Generated by Django 2.2.5 on 2020-03-05 03:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('searchqpapp', '0009_auto_20200304_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 5, 3, 8, 40, 508914, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='fileImage',
            field=models.ImageField(upload_to='searchqpapp/images'),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='filePdfField',
            field=models.FileField(upload_to='searchqpapp/pdf'),
        ),
    ]
