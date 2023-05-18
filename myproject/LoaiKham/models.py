from django.db import models

# Create your models here.
class LoaiKham(models.Model):
    LoaiKham_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
