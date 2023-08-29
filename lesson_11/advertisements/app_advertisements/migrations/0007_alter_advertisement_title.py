# Generated by Django 4.2.3 on 2023-08-27 13:26

import app_advertisements.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0006_alter_advertisement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=120, null=True, validators=[app_advertisements.models.validate_even], verbose_name='Заголовок'),
        ),
    ]
