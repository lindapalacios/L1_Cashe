from django.db import models
from datetime import datetime


class Data(models.Model):
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    data = models.TextField()
    author = models.TextField()
