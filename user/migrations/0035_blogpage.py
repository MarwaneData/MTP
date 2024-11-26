# Generated by Django 5.0.8 on 2024-11-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_blog_button_link_blog_button_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(default='Home - Discover Morocco Tours', max_length=255)),
                ('meta_description', models.TextField(default='Discover the beauty of Morocco with our exceptional tours and day trips. Contact us to plan your adventure today!')),
                ('meta_keywords', models.TextField(default='Morocco tours, day trips, desert tours, photography, luxury desert camp, Morocco travel')),
                ('hero_title', models.CharField(default='Discover the Magic of Morocco BY OUR BLOG.', max_length=255)),
                ('hero_subtitle', models.TextField(default='Bringing you the most captivating stories and insights about the enchanting land of Morocco.')),
                ('hero_image', models.ImageField(default='default_hero.jpg', upload_to='blog_hero/')),
            ],
        ),
    ]
