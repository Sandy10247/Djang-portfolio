from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=12)
    desciption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
