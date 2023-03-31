from django.db import models
from colorfield.fields import ColorField


class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags')

    date = models.DateField(auto_now=True)

    description = models.CharField(max_length=10000)
    link = models.CharField(max_length=1000, blank=True)
    github = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
