from django.db import models

# Create your models here.
class Question(models.Model):
    questionTitle=models.CharField(max_length=100)
    date=models.DateTimeField('date published')
    #IntegerField(default=10,min=1)

class Choice(models.Model):
    question=models.ForeignKey(Question)
    answer=models.CharField(max_length=200)
