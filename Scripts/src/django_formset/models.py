from django.db import models

# Create your models here.
class Programmer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name





class Language(models.Model):
    name = models.CharField(max_length=50)
    Programmer = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name
