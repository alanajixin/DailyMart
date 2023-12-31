# Generated by Django 4.2.6 on 2023-11-27 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('cartid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.cart')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.register')),
            ],
        ),
    ]
