# Generated by Django 2.2.5 on 2020-01-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchqpapp', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionPaperModel', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
