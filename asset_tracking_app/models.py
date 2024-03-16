from django.db import models
from employee_app.models import Employee
from assets_app.models import Asset

class AssetLog(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.CharField(max_length=50)
    condition_on_return = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.asset} - {self.employee} - {self.checkout_date}"

