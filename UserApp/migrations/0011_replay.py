# Generated by Django 4.2.6 on 2023-11-30 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0010_complaint_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('complaintid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.complaint')),
            ],
        ),
    ]
