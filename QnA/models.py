from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from users.forms import user



class Question(models.Model):
    qid=models.AutoField(primary_key=True)
    question_title=models.CharField(max_length=30)
    question_description=models.TextField(max_length=1024)
    posted_by=models.CharField(max_length=30,blank=True)
    date_posted=models.DateTimeField(auto_now_add= True)
    slug=models.SlugField(max_length=30)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.question_title)
        super(Question,self).save(*args,**kwargs)

class Answer(models.Model):
    aid=models.AutoField(primary_key=True)
    qid=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_description=models.TextField(max_length=5000)
    posted_on = models.DateTimeField(auto_now_add=True)
    posted_by=models.CharField(max_length=30)

    def save(self,*args,**kwargs):
        self.posted_by=user.username
        super(Answer,self).save(*args,**kwargs)

