from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=240, blank=True)
    image = models.ImageField(blank=True, upload_to='avatars/')
    location = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True,default="null")

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
 
    def display_name(self):
        return self.first_name + ' ' + self.lastname

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name+self.last_name)
        super().save(*args, **kwargs)   