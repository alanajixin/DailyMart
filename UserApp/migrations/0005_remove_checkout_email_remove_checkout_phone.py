# Generated by Django 4.2.6 on 2023-11-28 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='email',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='phone',
        ),
    ]
