from django.db import models

# Create your models here.
class Hruser(models.Model):
    name=models.CharField(max_length=50)
    uname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    company=models.CharField(max_length=50 , default=None ,null=True,blank=True)
    def __str__(self):
        return str(self.id)+" "+ self.uname
class Job(models.Model):
    title=models.CharField(max_length=50)
    profile=models.CharField(max_length=20)
    type=models.CharField(max_length=10)
    location=models.CharField(max_length=20)
    country=models.CharField(max_length=20 ,default="India")
    payout=models.CharField(max_length=25)
    desc=models.CharField(max_length=2000)
    date=models.DateField(auto_now=True)
    hr=models.ForeignKey(Hruser,on_delete=models.CASCADE,null=True)
    company=models.CharField(max_length=50,default=None,null=True,blank=True)

    def __str__(self):
        return str(self.id)