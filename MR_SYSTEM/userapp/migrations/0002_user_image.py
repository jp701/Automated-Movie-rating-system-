# Generated by Django 3.0.2 on 2021-03-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/profile.png', upload_to='images'),
        ),
    ]
