# Generated by Django 3.2.7 on 2021-10-03 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
