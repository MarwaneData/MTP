# Generated by Django 5.0.8 on 2024-11-05 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_blogpage_blogcontentblock'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPage',
            new_name='Blog',
        ),
    ]
