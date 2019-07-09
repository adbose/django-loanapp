
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    ammount = models.CharField(max_length=10)
    tenure = models.IntegerField()
    rate = models.IntegerField()
    Emi = models.IntegerField()
    class Meta:
        db_table="customer"