from django.db import models

class Example(models.Model):
    smth = models.IntegerField()
    smth2 = models.CharField(max_length=100)