# Generated by Django 5.0.8 on 2024-11-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_homepage_destinations_homepage_happy_travelers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='satisfaction_rate',
            field=models.DecimalField(decimal_places=0, default=100, help_text='Percentage satisfaction rate, e.g., 95.5', max_digits=5),
        ),
    ]
