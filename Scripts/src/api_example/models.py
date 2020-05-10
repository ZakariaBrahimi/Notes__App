from django.db import models

# Create your models here.


class Languages(models.Model):
    name = models.CharField(max_length=50)
    paradigme =  models.CharField( max_length=50)

    def __str__(self):
        return self.name