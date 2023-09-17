# Generated by Django 3.2.19 on 2023-09-17 10:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='rent_due_date',
        ),
        migrations.AddField(
            model_name='household',
            name='rent_due_day',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)]),
        ),
    ]
