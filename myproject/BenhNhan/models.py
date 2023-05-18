from django.db import models
from BacSi.models import BacSi
from LoaiKham.models import LoaiKham
from PhongKham.models import PhongKham

# Create your models here.
class BenhNhan(models.Model):
    BenhNhan_id = models.CharField(primary_key=True, max_length=20)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    BSPhuTrach = models.ForeignKey(BacSi, on_delete=models.CASCADE)
    LoaiKham_id = models.ForeignKey(LoaiKham, on_delete=models.CASCADE)
    PhongKham_id = models.ForeignKey(PhongKham, on_delete=models.CASCADE)