from django.db import models
from user.models import AppUser
from restaurant.models import MenuItem

class Order(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
