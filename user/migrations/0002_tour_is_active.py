# Generated by Django 5.0.8 on 2024-10-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Mark the tour as active or inactive'),
        ),
    ]
