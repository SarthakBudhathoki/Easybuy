# Generated by Django 4.0.1 on 2022-07-03 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_signupasseller_address_signupasseller_username_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
        migrations.AlterModelTable(
            name='product',
            table='Products',
        ),
    ]
