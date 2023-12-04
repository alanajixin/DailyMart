# Generated by Django 4.2.6 on 2023-11-27 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
        ('UserApp', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.product')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.register')),
            ],
        ),
    ]