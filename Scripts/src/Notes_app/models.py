from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Note(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    #slug    = models.SlugField(blank=True, null=True)
    content = models.TextField()
    created = models.DateTimeField(blank = True, default= datetime.datetime.now)
    active  = models.BooleanField(default=True)
    tags    = models.CharField(blank=True, max_length = 100)
    #img = models.ImageField(upload_to='notes_img', blank=True, null=True)

    def __str__(self):
        return self.title

