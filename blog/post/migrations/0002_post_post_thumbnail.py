# Generated by Django 4.1.7 on 2023-04-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
