from django.db import models

# models (classes)

class trails(models.Model):
    trail_id = models.IntegerField()
    trail_name = models.CharField(max_length=50)
    length_miles = models.FloatField()
    difficulty = models.CharField(max_length=15)
    completion_time = models.CharField(max_length=15)
    img_url = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=75)