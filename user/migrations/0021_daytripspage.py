# Generated by Django 5.0.8 on 2024-11-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_moroccotourspage_steps_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayTripsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(default='Home - Discover Morocco Tours', max_length=255)),
                ('meta_description', models.TextField(default='Discover the beauty of Morocco with our exceptional tours and day trips.')),
                ('meta_keywords', models.TextField(default='Morocco tours, day trips, desert tours, photography, luxury desert camp, Morocco travel')),
                ('hero_title', models.CharField(default='Exciting and Affordable Morocco Day Trips', max_length=255)),
                ('hero_paragraph', models.TextField(default='Create unforgettable memories with our Marrakech Desert Trips.')),
                ('hero_image', models.ImageField(default='default_hero.jpg', upload_to='day_trips/')),
                ('display_hero_button', models.BooleanField(default=True)),
                ('hero_button_text', models.CharField(default='Request Tour', max_length=50)),
                ('show_services_section', models.BooleanField(default=True)),
                ('service_title1', models.CharField(default='Licensed Guides', max_length=255)),
                ('service_image1', models.ImageField(default='default_service1.jpg', upload_to='day_trips/services/')),
                ('service_description1', models.CharField(default='Officially Licensed Guides', max_length=255)),
                ('service_title2', models.CharField(default='Guided Walking Tour', max_length=255)),
                ('service_image2', models.ImageField(default='default_service2.jpg', upload_to='day_trips/services/')),
                ('service_description2', models.CharField(default='Guided Walking Tour', max_length=255)),
                ('service_title3', models.CharField(default='Flexible Rescheduling', max_length=255)),
                ('service_image3', models.ImageField(default='default_service3.jpg', upload_to='day_trips/services/')),
                ('service_description3', models.CharField(default='Flexible Rescheduling', max_length=255)),
                ('show_best_day_trips_section', models.BooleanField(default=True)),
                ('best_day_trips_title', models.CharField(default='The Best Morocco Day Trips', max_length=255)),
                ('show_all_day_trips_section', models.BooleanField(default=True)),
                ('all_day_trips_title', models.CharField(default='All Private Excursions and Day Trips', max_length=255)),
                ('show_blog_section', models.BooleanField(default=True)),
                ('blog_title', models.CharField(default='Explore Morocco Through Our Blogs', max_length=255)),
                ('blog_paragraph', models.TextField(default='At Discover Morocco Tours, we specialize in organizing exceptional tours across the beautiful landscapes of Morocco.')),
                ('blog_image', models.ImageField(default='default_blog.jpg', upload_to='day_trips/')),
                ('show_unique_experiences_section', models.BooleanField(default=True)),
                ('unique_experiences_title', models.CharField(default='Unique Experiences You Can Only Have in Morocco', max_length=255)),
                ('unique_experiences_paragraph', models.TextField(default='At Discover Morocco Tours, we specialize in organizing exceptional tours across the beautiful landscapes of Morocco.')),
                ('unique_experiences_image', models.ImageField(default='default_experience.jpg', upload_to='day_trips/')),
            ],
        ),
    ]
