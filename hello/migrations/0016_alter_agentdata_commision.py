# Generated by Django 4.2.4 on 2023-08-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0015_alter_crossselldata_additional_households_with_vehicles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentdata',
            name='commision',
            field=models.IntegerField(),
        ),
    ]