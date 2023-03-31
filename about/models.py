from django.db import models
from model_extensions.models import SingleActive


class Bio(SingleActive):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title


class Photo(SingleActive):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='profile/')
    date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title


