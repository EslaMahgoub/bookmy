# Generated by Django 3.2.7 on 2021-10-03 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertyreview',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='children',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
    ]
