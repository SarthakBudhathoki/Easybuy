# Generated by Django 4.0.1 on 2022-06-18 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_editorders_customer_alter_editorders_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editorders',
            name='status',
        ),
    ]