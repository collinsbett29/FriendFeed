from django.db import models
from django.utils.text import slugify


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='DEFAULT VALUE')
    slug = models.SlugField(allow_unicode=True, unique=True)
    image = models.ImageField(upload_to='groups/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)