# Generated by Django 5.0.8 on 2024-11-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0055_alter_aboutpage_options_alter_blog_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographertourpage',
            name='destination_paragraphs',
            field=models.TextField(blank=True, help_text='Description markting for section', null=True),
        ),
    ]
