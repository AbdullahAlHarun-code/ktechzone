# Generated by Django 4.1.5 on 2023-01-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productvariation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='web/products/variations/images/'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]