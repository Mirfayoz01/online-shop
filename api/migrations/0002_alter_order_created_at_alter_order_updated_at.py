# Generated by Django 5.1.6 on 2025-02-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='create_at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='update_at'),
        ),
    ]
