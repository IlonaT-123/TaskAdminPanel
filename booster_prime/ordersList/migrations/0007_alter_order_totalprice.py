# Generated by Django 4.2.5 on 2023-09-16 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersList', '0006_alter_city_options_alter_fuel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalPrice',
            field=models.IntegerField(blank=0, verbose_name='Сумма'),
        ),
    ]