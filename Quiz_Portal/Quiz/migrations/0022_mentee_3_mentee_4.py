# Generated by Django 3.0.3 on 2020-05-13 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0021_auto_20200513_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phn_num', models.CharField(max_length=10, unique=True)),
                ('batch_num', models.CharField(max_length=1)),
                ('ans1', models.CharField(max_length=200)),
                ('ans2', models.CharField(max_length=200)),
                ('ans3', models.CharField(max_length=200)),
                ('ans4', models.CharField(max_length=200)),
                ('ans5', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phn_num', models.CharField(max_length=10, unique=True)),
                ('batch_num', models.CharField(max_length=1)),
                ('ans1', models.CharField(max_length=200)),
                ('ans2', models.CharField(max_length=200)),
                ('ans3', models.CharField(max_length=200)),
                ('ans4', models.CharField(max_length=200)),
                ('ans5', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
