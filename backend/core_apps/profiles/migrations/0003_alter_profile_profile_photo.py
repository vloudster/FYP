# Generated by Django 4.0.4 on 2022-04-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='/default_photo.png', upload_to='', verbose_name='profile_photo'),
        ),
    ]
