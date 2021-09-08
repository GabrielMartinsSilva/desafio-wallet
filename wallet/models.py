from django.db import models


class Cashback(models.Model):
    customer = models.JSONField()
    products = models.JSONField()
    total = models.IntegerField()
    sold_at = models.DateTimeField(blank=True, null=True)
