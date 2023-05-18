from django.db import models
from LoaiKham.models import LoaiKham
from PhongKham.models import PhongKham

class BacSi(models.Model):
    BacSi_id = models.CharField(primary_key=True, max_length=50)
    Name = models.CharField(max_length=50)
    LoaiKham_id = models.ForeignKey(LoaiKham, on_delete=models.CASCADE)
    PhongKham_id = models.ForeignKey(PhongKham, on_delete=models.CASCADE)
