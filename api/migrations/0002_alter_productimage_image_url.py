# Generated by Django 5.1.6 on 2025-02-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image_url',
            field=models.ImageField(upload_to='avatars/'),
        ),
    ]
