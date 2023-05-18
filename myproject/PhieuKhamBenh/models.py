from django.db import models

class PhieuKhamBenh(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    MaBN = models.CharField(max_length= 30)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
