# Generated by Django 3.0.3 on 2020-05-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_question_ca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phn_num', models.IntegerField()),
                ('batch_num', models.IntegerField()),
            ],
        ),
    ]
