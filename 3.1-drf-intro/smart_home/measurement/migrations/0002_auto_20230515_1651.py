# Generated by Django 3.1.2 on 2023-05-15 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='measurement.sensor'),
        ),
    ]
