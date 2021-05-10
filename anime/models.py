from django.db import models
class APIData(models.Model):
    title = models.CharField(max_length=50)

