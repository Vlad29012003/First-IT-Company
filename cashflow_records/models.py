from django.db import models
from directories.models import Status, Type, Category, SubCategory

class CashFlowRecord(models.Model):
    created_at = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.created_at} | {self.status} | {self.type} | {self.category} | {self.subcategory} | {self.amount}₽'
