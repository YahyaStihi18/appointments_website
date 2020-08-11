from django.db import models
from django.contrib.auth.models import User
import datetime


class Appointment(models.Model):
    time_choice = [
        ('09:00-10:00','09:00-10:00'),
        ('10:00-11:00','10:00-11:00'),
        ('11:00-12:00','11:00-12:00'),
        ('14:00-15:00','14:00-15:00'),
        ('15:00-16:00','15:00-16:00'),
        ('16:00-17:00','16:00-17:00'),

        ]
    service_choice = [
        ('فحص طبي','فحص طبي'),
        ('تصوير بالاشعة','تصوير بالاشعة'),
        ('اكمال علاج سابق','اكمال علاج سابق'),
        ('استخراج وثائق طبية','استخراج وثائق طبية'),

        ]

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.CharField(max_length=200,choices=time_choice)
    service = models.CharField(max_length=200,choices=service_choice)
    on_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name+' '+self.last_name


