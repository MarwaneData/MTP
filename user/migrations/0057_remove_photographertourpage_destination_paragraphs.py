# Generated by Django 5.0.8 on 2024-11-22 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0056_photographertourpage_destination_paragraphs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographertourpage',
            name='destination_paragraphs',
        ),
    ]
