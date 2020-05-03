from django.db import models
class Mentee(models.Model):
    name=models.CharField(max_length=50)
    phn_num=models.CharField(max_length=10,unique=True)
    batch_num=models.CharField(max_length=1)
    ans1=models.CharField(max_length=200)
    ans2=models.CharField(max_length=200)
    ans3=models.CharField(max_length=200)
    ans4=models.CharField(max_length=200)
    ans5=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    id=models.CharField(max_length=1,default=1,primary_key=True)
    ques=models.CharField(max_length=200)
    opt1=models.CharField(max_length=200)
    opt2=models.CharField(max_length=200)
    opt3=models.CharField(max_length=200)
    opt4=models.CharField(max_length=200)
    ca=models.CharField(max_length=200)

    def __str__(self):
        return self.ques


