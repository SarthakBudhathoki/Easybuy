# Generated by Django 4.0.1 on 2022-07-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_remove_product_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('messgae', models.CharField(max_length=500)),
            ],
        ),
    ]