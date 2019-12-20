# Generated by Django 3.0 on 2019-12-18 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingleRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('booked_at', models.DateTimeField(default=datetime.datetime(2019, 12, 18, 20, 47, 59, 313600))),
                ('booked_end', models.DateTimeField(blank=True)),
                ('pic', models.ImageField(upload_to='')),
            ],
        ),
    ]