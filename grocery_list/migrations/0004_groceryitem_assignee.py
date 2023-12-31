# Generated by Django 3.2.19 on 2023-10-08 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grocery_list', '0003_grocerylist_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_grocery_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
