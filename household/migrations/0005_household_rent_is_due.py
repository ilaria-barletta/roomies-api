# Generated by Django 3.2.19 on 2023-10-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0004_rename_household_householdmember_household'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='rent_is_due',
            field=models.BooleanField(default=False),
        ),
    ]
