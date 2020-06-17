from django.conf import settings
from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    mobile = models.TextField()


    def __str__(self):
        return self.name
