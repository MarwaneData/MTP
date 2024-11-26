# Generated by Django 5.0.8 on 2024-11-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_desertcamppage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(default='Home - Discover Morocco Tours', max_length=255)),
                ('meta_description', models.TextField(default='Discover the beauty of Morocco with our exceptional tours and day trips.')),
                ('meta_keywords', models.TextField(default='Morocco tours, day trips, desert tours, photography, luxury desert camp, Morocco travel')),
                ('hero_title', models.CharField(default='About Photographer Morocco Tours', max_length=255)),
                ('hero_paragraph', models.CharField(default='Create unforgettable memories with our services', max_length=255)),
                ('hero_image', models.ImageField(default='default_hero.jpg', upload_to='about/')),
                ('video_section_title', models.CharField(default='Explore Morocco Tours', max_length=255)),
                ('video_section_description', models.TextField(default='Embark on a journey through the vibrant landscapes of Morocco...')),
                ('video_url', models.URLField(default='https://www.youtube.com/embed/E2UrxR61CYM')),
                ('first_section_title', models.CharField(default='Your Gateway to Morocco', max_length=255)),
                ('first_section_text', models.TextField(default='At Discover Morocco Tours, we specialize in organizing exceptional tours across Morocco.')),
                ('first_section_image', models.ImageField(default='default_first_section.jpg', upload_to='about/')),
                ('services_title', models.CharField(default='Services We Offer', max_length=255)),
                ('service_title1', models.CharField(default='Cultural Immersion', max_length=255)),
                ('service_description1', models.TextField(default="Our cultural tours take you deep into the heart of Morocco's history and traditions.")),
                ('service_image1', models.ImageField(default='default_service1.jpg', upload_to='about/services/')),
                ('service_title2', models.CharField(default='Adventure Excursions', max_length=255)),
                ('service_description2', models.TextField(default="Experience thrilling adventures across Morocco's landscapes.")),
                ('service_image2', models.ImageField(default='default_service2.jpg', upload_to='about/services/')),
                ('service_title3', models.CharField(default='Luxury Desert Camps', max_length=255)),
                ('service_description3', models.TextField(default='Stay in our luxurious desert camps for an unforgettable experience.')),
                ('service_image3', models.ImageField(default='default_service3.jpg', upload_to='about/services/')),
                ('client_care_title', models.CharField(default='How We Care for Our Clients', max_length=255)),
                ('client_care_text', models.TextField(default='At Morocco Photographer Tours, our clients are at the heart of everything we do.')),
                ('client_care_image', models.ImageField(default='default_client_care.jpg', upload_to='about/')),
                ('testimonials_title', models.CharField(default='Hear from Our Travelers', max_length=255)),
                ('testimonial1_content', models.TextField(default='Sometimes I think the surest sign that intelligent life exists...')),
                ('testimonial1_image', models.ImageField(default='default_testimonial1.jpg', upload_to='about/testimonials/')),
                ('testimonial1_name', models.CharField(default='Steve', max_length=255)),
                ('testimonial1_source', models.CharField(default='TripAdvisor', max_length=255)),
                ('testimonial2_content', models.TextField(default='Exploring Morocco with this tour was an unforgettable experience...')),
                ('testimonial2_image', models.ImageField(default='default_testimonial2.jpg', upload_to='about/testimonials/')),
                ('testimonial2_name', models.CharField(default='Maxime', max_length=255)),
                ('testimonial2_source', models.CharField(default='Instagram', max_length=255)),
                ('testimonial3_content', models.TextField(default='The hospitality and depth of experience offered on this tour made Morocco come alive...')),
                ('testimonial3_image', models.ImageField(default='default_testimonial3.jpg', upload_to='about/testimonials/')),
                ('testimonial3_name', models.CharField(default='Stephen', max_length=255)),
                ('testimonial3_source', models.CharField(default='TripAdvisor', max_length=255)),
            ],
        ),
    ]
