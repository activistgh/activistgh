# Generated by Django 5.0.6 on 2024-11-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_cartobject_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]