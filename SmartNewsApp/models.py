from django.db import models

class Date(models.Model):
    date = models.CharField(max_length=50)

class Source(models.Model):
    code = models.CharField(max_lenght = 25, help_text='Enter source identification')
    name = models.CharField(max_lenght = 25)
    description = models.TextField()
    category = models.CharField(max_lenght = 20)
    language = models.CharField(max_lenght = 4)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
