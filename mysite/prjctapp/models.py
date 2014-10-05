from django.db import models
from django.utils import timezone
import datetime

    # Create your models here.

    
class User(models.Model):
    user_photo = models.FileField(upload_to='uploads%Y%m%d',null=True,blank=True)
    user_name = models.CharField(primary_key=True,max_length=200)
    password = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published',default=timezone.now)

    def __str__(self):
        return self.user_photo.url
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    
    def __str__(self):
        return self.user_name

    


class Message(models.Model):
    message_text = models.CharField(max_length=200)
    send_image_or_pdf = models.ForeignKey('Upload',related_name='+',null=True,blank=True)
    message_from = models.ForeignKey('User',related_name='+')
    message_to = models.ForeignKey('User',related_name='+')
    pub_date = models.DateTimeField('date published',default=timezone.now)
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    def __str__(self):
        return self.message_text
    
class Upload(models.Model):
    upload = models.FileField(upload_to='uploads%Y%m%d')
    pub_date = models.DateTimeField('date published',default=timezone.now)

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    
    def __str__(self):
        return self.upload.url 

#class Message_sendto(models.Model):
        
