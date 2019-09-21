from django.db import models


class UrlEntry(models.Model):
    short_id = models.CharField(max_length=50)
    value = models.CharField(max_length=2048)
    created_on = models.DateTimeField('date added')
