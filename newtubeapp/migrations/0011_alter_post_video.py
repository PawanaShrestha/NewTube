# Generated by Django 4.0.4 on 2022-05-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtubeapp', '0010_alter_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(upload_to='videos/%y'),
        ),
    ]
