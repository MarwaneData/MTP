# Generated by Django 5.0.8 on 2024-11-03 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_remove_moroccotourspage_hero_button_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moroccotourspage',
            options={'verbose_name': 'Morocco Tours Page', 'verbose_name_plural': 'Morocco Tours Page'},
        ),
        migrations.RemoveField(
            model_name='moroccotourspage',
            name='service_description1',
        ),
        migrations.RemoveField(
            model_name='moroccotourspage',
            name='service_description2',
        ),
        migrations.RemoveField(
            model_name='moroccotourspage',
            name='service_description3',
        ),
    ]
