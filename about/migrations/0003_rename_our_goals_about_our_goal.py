# Generated by Django 3.2.7 on 2021-10-03 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20211003_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='our_goals',
            new_name='our_goal',
        ),
    ]