# Generated by Django 3.0.2 on 2021-03-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_auto_20210313_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='production',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]