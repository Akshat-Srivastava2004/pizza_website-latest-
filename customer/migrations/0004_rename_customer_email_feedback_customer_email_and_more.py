# Generated by Django 4.2.3 on 2023-10-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Customer_email',
            new_name='customer_email',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='Customer_name',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='messsage',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cvv',
            field=models.IntegerField(),
        ),
    ]
