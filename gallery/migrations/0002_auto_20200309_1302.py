# Generated by Django 3.0.4 on 2020-03-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile-pic/default-no-profile-pic.jpg', upload_to='profile-pic/'),
        ),
    ]
