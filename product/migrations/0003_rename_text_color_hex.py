# Generated by Django 4.1.5 on 2023-01-05 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_capacity_color_condition_productvariation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='text',
            new_name='hex',
        ),
    ]
