from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default=None, blank=True, null=True)
    instructor = models.CharField(max_length=255)
    duration = models.IntegerField()
    price = models.FloatField()
