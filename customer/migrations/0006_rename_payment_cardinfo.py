# Generated by Django 4.2.3 on 2023-10-20 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_payment_card_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payment',
            new_name='CardInfo',
        ),
    ]
