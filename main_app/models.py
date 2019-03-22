from django.db import models

# Create your models here.

class Item(models.Model):
  description = models.TextField(max_length=100)

  def __str__(self):
    return self.description