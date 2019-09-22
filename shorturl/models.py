from django.db import models


class UrlEntry(models.Model):
    # specifying unique constraint will force django to create index on this field
    # we need to have an index in order to make sure that search by short_id is efficient
    short_id = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=2048)
    created_on = models.DateTimeField('date added')
