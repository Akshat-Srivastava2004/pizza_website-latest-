# Generated by Django 4.2.3 on 2023-10-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_rename_customer_email_feedback_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=16),
        ),
    ]
