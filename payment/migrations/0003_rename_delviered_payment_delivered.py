# Generated by Django 5.0.6 on 2024-10-27 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_payment_delviered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='delviered',
            new_name='delivered',
        ),
    ]
