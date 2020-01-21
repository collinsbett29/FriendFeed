from django.db import models
from django.contrib.auth.models import AbstractUser
# if you have space in string it will fill with dashes etc so your browser can read it
from django.utils.text import slugify


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=240, blank=True)
    image = models.ImageField(blank=True, upload_to='avatars/')
    location = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def display_name(self):
        return self.first_name + ' ' + self.lastname

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # when person types in group name with spaces this slugify will
        self.slug = slugify(self.first_name+self.last_name)
    # change the name so it can be used in URL by browser
        super().save(*args, **kwargs)