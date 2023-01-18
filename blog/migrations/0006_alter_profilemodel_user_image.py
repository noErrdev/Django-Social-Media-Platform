# Generated by Django 4.1.4 on 2023-01-18 06:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_created_category_discription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='user_image',
            field=models.ImageField(default='media/default.png', upload_to='media', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
