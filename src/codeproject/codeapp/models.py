from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class USER(User):
    def __str__(self):
        return self.username


class Developer(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE,primary_key=True)
    career = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    portfolioweb = models.URLField()
    location = models.CharField(max_length=30)
    skills = models.CharField(max_length=500)
    githublink = models.URLField(blank=True, null=True)
    tweetlink = models.URLField(blank=True, null=True)
    fblink = models.URLField(blank=True, null=True)
    instalink = models.URLField(blank=True, null=True)
    tweetlink = models.URLField(blank=True, null=True)
    youtubelink = models.URLField(blank=True, null=True) 
    
    
class Experience(models.Model):
    whose = models.ForeignKey(Developer,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=30)
    aff_company = models.CharField(max_length=30)
    loc_company = models.CharField(max_length=30)
    frm_date = models.DateField()
    to_date = models.DateField()
    job_des = models.CharField(max_length=500)
    

class Education(models.Model):
    whose = models.ForeignKey(Developer,on_delete=models.CASCADE)
    degree = models.CharField(max_length=30)
    college = models.CharField(max_length=30)
    frm_date = models.DateField()
    to_date = models.DateField()

    
class Post(models.Model):
    whose = models.ForeignKey(Developer,on_delete=models.CASCADE)
    text = models.TextField()