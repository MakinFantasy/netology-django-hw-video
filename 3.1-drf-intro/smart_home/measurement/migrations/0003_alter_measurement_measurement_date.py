# Generated by Django 4.0.4 on 2022-04-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_temperature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
