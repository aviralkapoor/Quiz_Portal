# Generated by Django 3.0.3 on 2020-05-03 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_auto_20200503_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='ques',
        ),
        migrations.AddField(
            model_name='mentee',
            name='ques',
            field=models.ManyToManyField(to='Quiz.Question'),
        ),
    ]