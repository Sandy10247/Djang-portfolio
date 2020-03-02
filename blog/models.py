from django.db import models

# Create your models here.
class  Blog(models.Model):
    title = models.CharField(max_length=20, blank=False,)
    description = models.TextField()
    date = models.DateField()

    # Description
    def __str__(self):
        return self.title
