from django.db import models

class Date(models.Model):
    date = models.CharField(max_length=50)

class Source(models.Model):
    code = models.CharField(max_length = 25, help_text='Enter source identification')
    name = models.CharField(max_length = 25)
    description = models.TextField()
    category = models.CharField(max_length = 20)
    language = models.CharField(max_length = 4)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

class Country(models.Model):
    country_code = models.CharField(max_length=25)

class Topic(models.Model):
    name = models.CharField(max_length=25)

class Statistic(models.Model):
    statistic_code = models.IntegerField()
    concept = models.TextField()
    date = models.ForeignKey('Date', on_delete=models.CASCADE)
    name = models.ForeignKey('Topic', on_delete=models.CASCADE)

class News(models.Model):
    code = models.ForeignKey('Source', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField()
    publishedAt = models.ForeignKey('Date', on_delete=models.CASCADE)
    content = models.TextField()
    topics = models.ManyToManyField('Topic', related_name='news')
