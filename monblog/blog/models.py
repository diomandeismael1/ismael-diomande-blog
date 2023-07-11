from django.db import models
from django.utils import timezone

# Create your models here.
class Publication(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    publication_title= models.CharField(max_length=100)
    publication_text=models.CharField(max_length=500)
    pub_date=timezone.now()

class Author(models.Model):
    name= models.CharField(max_length=100)
    description=models.CharField(max_length=500)
