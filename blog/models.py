from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank = True, null = True)
    date = models.DateField(auto_now_add=True)

    def save(self,*args,**kwargs):
        super(Post,self).save(*args,**kwargs)
        return self

    def __str__(self):
        return self.title+'|'+str(self.author)
    def get_absolute_url(self):
         return reverse('home')

class PreviousPost(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    body = RichTextField(blank = True, null = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    