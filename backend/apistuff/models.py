from django.db import models
from django.contrib.postgres.fields import ArrayField


# add validation

# Create your models here.
class SampleData(models.Model):
    data = ArrayField(base_field=ArrayField(base_field=models.IntegerField()))
    category = models.CharField(max_length=1)
