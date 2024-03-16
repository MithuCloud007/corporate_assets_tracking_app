from django.db import models
from company_app.models import Company

class Asset(models.Model):
    ASSET_TYPE = [
        ('PHONE', 'PHONE'),
        ('LAPTOP', 'LAPTOP'),
        ('TABLETS', 'TABLETS'),
        ('OTHERS', 'OTHERS')
        ]
    serial_number = models.CharField(max_length=50, unique=True)
    asset_type = models.CharField(max_length=50,choices=ASSET_TYPE)
    condition = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.serial_number

