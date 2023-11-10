# Generated by Django 4.2.3 on 2023-10-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_rename_payment_cardinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
            ],
        ),
    ]