from django.db import models

class Studnet(models.Model):
    name = models.CharField(max_length = 50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
