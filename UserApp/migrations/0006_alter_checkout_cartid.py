# Generated by Django 4.2.6 on 2023-11-28 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0005_remove_checkout_email_remove_checkout_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cartid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.cart'),
        ),
    ]