from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null= True, on_delete = models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_dp = models.ImageField(null=True, blank=True, upload_to = "profile_dps/")

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length = 255)
    uploader = models.CharField(max_length=200, blank=False, default = "admin")
    video = models.FileField(upload_to = "videos/%y")
    thumbnail = models.FileField(upload_to = "thumbnails/")
    description = models.TextField()
    hashtags = models.CharField(max_length=255, default="#NewTube")
    upload_date = models.DateField(default = date.today)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.uploader)

    @property
    def days_ago(self):
        days_ago_int = date.today() - self.upload_date
        days_ago_str = str(days_ago_int).split(",", 1)[0]
        if days_ago_str == "0:00:00":
            return "0 days"
        else:
            return days_ago_str

    def get_absolue_url(self):
        return reverse('home')
    
class Ads(models.Model):
    ad = models.FileField(upload_to = "ads/")
    ad_title = models.CharField(max_length = 255, null = True, blank= True)

    def __str__(self):
        return self.ad_title
