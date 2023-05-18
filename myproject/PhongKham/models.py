from django.db import models

class PhongKham(models.Model):
    PhongKham_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
