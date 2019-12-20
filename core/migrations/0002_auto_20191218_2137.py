# Generated by Django 3.0 on 2019-12-18 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleroom',
            name='booked_at',
            field=models.DateField(default=datetime.date(2019, 12, 18)),
        ),
        migrations.AlterField(
            model_name='singleroom',
            name='booked_end',
            field=models.DateField(blank=True),
        ),
    ]
