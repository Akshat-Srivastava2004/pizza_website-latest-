# Generated by Django 4.2.3 on 2023-10-24 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0007_pizzainfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzainfo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pizzas_ordered', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
