# Generated by Django 3.2.7 on 2021-10-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='settings/')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('description', models.TextField()),
                ('fb_link', models.URLField(max_length=255)),
                ('twitter_link', models.URLField(max_length=255)),
                ('instagram_link', models.URLField(max_length=255)),
            ],
        ),
    ]
