# Generated by Django 4.1.5 on 2023-01-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='portal/image'),
        ),
    ]
