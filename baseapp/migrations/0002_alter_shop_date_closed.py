# Generated by Django 4.1.7 on 2023-03-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="date_closed",
            field=models.DateField(null=True),
        ),
    ]
