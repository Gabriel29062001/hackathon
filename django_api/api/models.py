from django.db import models

# Create your models here.
class PredictionValue(models.Model):
    ecg_value = models.FloatField()
    total_value = models.FloatField()

class  ImageEcg(models.Model):
    image = models.ImageField()