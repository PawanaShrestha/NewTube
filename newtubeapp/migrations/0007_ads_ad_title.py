# Generated by Django 4.0.4 on 2022-05-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtubeapp', '0006_rename_thumbnail_ads_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='ad_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
