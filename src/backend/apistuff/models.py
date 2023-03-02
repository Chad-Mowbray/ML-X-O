from django.db import models
from django.contrib.postgres.fields import ArrayField


class SampleData(models.Model):
    data = ArrayField(base_field=models.IntegerField())
    category = models.CharField(max_length=1)

class TrainedModel(models.Model):
    model = models.BinaryField()
    ts = models.DateTimeField(auto_now_add=True)