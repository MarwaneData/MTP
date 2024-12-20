# Generated by Django 5.0.8 on 2024-10-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_camp_booking_url_remove_camp_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(default='Home - Discover Morocco Tours', max_length=255)),
                ('meta_description', models.TextField(default='Discover the beauty of Morocco with our exceptional tours and day trips. Contact us to plan your adventure today!')),
                ('meta_keywords', models.TextField(default='Morocco tours, day trips, desert tours, photography, luxury desert camp, Morocco travel')),
                ('hero_title', models.CharField(default='Exciting and Affordable Morocco Desert Tours', max_length=255)),
                ('hero_paragraph', models.TextField(default='Create unforgettable memories with our Marrakech Desert Trips.')),
                ('hero_image', models.ImageField(default='default_hero.jpg', upload_to='homepage/')),
                ('display_hero_button', models.BooleanField(default=True)),
                ('hero_button_text', models.CharField(default='Request Tour', max_length=50)),
                ('hero_button_url', models.URLField(default='#')),
                ('show_tours_section', models.BooleanField(default=True)),
                ('tours_section_title', models.CharField(default='Private Morocco Desert Tours', max_length=255)),
                ('show_excursions_section', models.BooleanField(default=True)),
                ('excursions_section_title', models.CharField(default='PRIVATE EXCURSIONS AND DAY TRIPS', max_length=255)),
                ('show_photoshoots_section', models.BooleanField(default=True)),
                ('photoshoots_section_title', models.CharField(default='Photoshoots Tours', max_length=255)),
                ('show_about_section', models.BooleanField(default=True)),
                ('about_title', models.CharField(default='Behind the Scenes, Who we are?', max_length=255)),
                ('about_paragraph', models.TextField(default='At Discover Morocco Tours, we specialize in organizing exceptional tours across the beautiful landscapes of Morocco.')),
                ('about_image', models.ImageField(default='default_about.jpg', upload_to='homepage/')),
                ('show_comfort_section', models.BooleanField(default=True)),
                ('comfort_title', models.CharField(default='Enjoy Your Comfort Tour of Morocco', max_length=255)),
                ('comfort_paragraph', models.TextField(default='At Discover Morocco Tours, we specialize in organizing exceptional tours across the beautiful landscapes of Morocco.')),
                ('comfort_image', models.ImageField(default='default_comfort.jpg', upload_to='homepage/')),
            ],
        ),
    ]
