from django.db import models

# Create your models here.

class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ('created',)
