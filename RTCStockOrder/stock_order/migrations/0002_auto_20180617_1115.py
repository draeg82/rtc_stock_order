# Generated by Django 2.0.5 on 2018-06-17 10:15

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('stock_order', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prouct',
            new_name='Product',
        ),
    ]
