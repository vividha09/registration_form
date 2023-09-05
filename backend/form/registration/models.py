from django.db import models

class React(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.IntegerField(null = True)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)