# Generated by Django 4.1.7 on 2023-03-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0005_alter_shop_tel_main_alter_shop_tel_man"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="tel_main",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="shop",
            name="tel_man",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
