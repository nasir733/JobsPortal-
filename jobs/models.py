from django.db import models

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    def __str__(self):
        return self.title