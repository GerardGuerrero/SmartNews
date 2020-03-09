from django.db import models

class Date(models.Model):
    date = models.CharField(max_length=50)

class Country(models.Model):
    country_code = models.CharField(max_length=25)

class Topic(models.Model):
    name = models.CharField(max_length=25)

class Statistic(models.Model):
    statistic_code = models.IntegerField()
    concept = models.TextField()
    date = models.ForeignKey('Date', on_delete=models.CASCADE)
    name = models.ForeignKey('Topic', on_delete=models.CASCADE)
