from django.db import models

# Create your models here.
class CurrentJoke(models.Model):
    text = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)

