# Generated by Django 3.0.8 on 2020-07-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artgen', '0011_remove_art_filepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image_1',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='art',
            name='image_2',
            field=models.FileField(upload_to='images/'),
        ),
    ]
