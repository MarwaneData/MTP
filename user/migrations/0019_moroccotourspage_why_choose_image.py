# Generated by Django 5.0.8 on 2024-11-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_moroccotourspage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moroccotourspage',
            name='why_choose_image',
            field=models.ImageField(default='default_hero.jpg', upload_to='morocco_tours/'),
        ),
    ]
