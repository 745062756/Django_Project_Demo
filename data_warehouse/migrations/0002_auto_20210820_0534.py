# Generated by Django 3.2.6 on 2021-08-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payer',
            name='city',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='payer',
            name='first_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='payer',
            name='last_name',
            field=models.CharField(max_length=32),
        ),
    ]
