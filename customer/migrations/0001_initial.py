# Generated by Django 4.2.3 on 2023-10-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=100)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=4)),
            ],
        ),
    ]
