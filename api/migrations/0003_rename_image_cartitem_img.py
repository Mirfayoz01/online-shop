# Generated by Django 5.1.6 on 2025-02-26 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_img_cartitem_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='image',
            new_name='img',
        ),
    ]
