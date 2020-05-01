from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
import datetime

# Create your models here.
class Note(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    slug    = models.SlugField(blank=True, null=True)
    title   = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(blank = True, default= datetime.datetime.now)
    active  = models.BooleanField(default=True)
    tags    = models.CharField(blank=True, max_length = 100)
    img     = models.ImageField(upload_to='notes_img', blank=True, null=True)
    
    def save(self, *arg, **kwarg):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Note, self).save(*arg, **kwarg)

    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Profile(models.Model):
    user_img = models.ImageField(upload_to='user_img', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    #my_notes = models.ForeignKey(Note, on_delete=models.CASCADE)
    slug    = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.user.username

    def save(self, *arg, **kwarg):
        if not self.slug :
            self.slug = slugify(self.user)
        super(Profile, self).save(*arg, **kwarg)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs["instance"])

post_save.connect(create_profile, sender=User)



