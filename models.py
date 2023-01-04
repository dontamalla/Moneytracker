from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    spending_category = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.ManyToManyField(User)