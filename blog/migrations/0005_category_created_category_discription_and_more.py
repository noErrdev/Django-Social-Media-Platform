# Generated by Django 4.1.4 on 2023-01-16 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_postmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
