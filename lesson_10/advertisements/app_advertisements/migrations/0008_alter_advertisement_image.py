# Generated by Django 4.2.3 on 2023-08-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0007_alter_advertisement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, upload_to='advertisements/', verbose_name='изображение'),
        ),
    ]
