# Generated by Django 5.0.8 on 2024-11-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_photographertourpage_package'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photographertourpage',
            options={'verbose_name': 'Photographer Tour Page', 'verbose_name_plural': 'Photographer Tour Pages'},
        ),
        migrations.RenameField(
            model_name='package',
            old_name='page',
            new_name='photographer_tour_page',
        ),
        migrations.AlterField(
            model_name='package',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='package',
            name='duration',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='editing_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='original_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
