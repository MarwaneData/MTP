# Generated by Django 5.0.8 on 2024-11-03 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_moroccotourspage_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moroccotourspage',
            name='hero_button_url',
        ),
    ]
