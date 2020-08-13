from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
sex_choice = [
        ('ذكر','ذكر'),
        ('انثى','انثى'),
        ]
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField('الاسم',max_length=200)
    last_name = models.CharField('اللقب',max_length=200)
    phone = models.BigIntegerField('الهاتف',null=True,blank=False)
    address = models.CharField('العنوان',max_length=200,null=True,blank=False)
    date_of_birth = models.DateField('تاريخ الميلاذ')
    sex = models.CharField('الجنس',choices=sex_choice,max_length=200)

    def __str__(self):
        return self.user.username
