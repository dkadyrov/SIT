# Generated by Django 3.0.8 on 2020-07-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artgen', '0006_auto_20200724_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='filepath',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='art',
            name='image_1',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='art',
            name='image_2',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
