from django.db import models # type: ignore

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()

