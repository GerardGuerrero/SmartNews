from django.db import models

class Date(models.Model):
    date = models.CharField(max_length=50)

class News(models.Model):
    code = models.ForeignKey('Source', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField()
    publishedAt = models.ForeignKey('Date', on_delete=models.CASCADE)
    content = models.TextField()
    topics = models.ManyToManyField('Topic', related_name='name')
