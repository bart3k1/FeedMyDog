# Generated by Django 3.0.4 on 2020-03-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendog', '0002_remove_addcallendog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcallendog',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='addcallendog',
            name='stop_date',
            field=models.DateField(),
        ),
    ]
