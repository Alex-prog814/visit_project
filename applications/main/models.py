from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Worker(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return self.name


class TradePoint(models.Model):
    title = models.CharField(max_length=100)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, related_name='trade_point')

    def __str__(self):
        return self.title


class Visit(models.Model):
    phone_number = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE, related_name='visit')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.trade_point.title
