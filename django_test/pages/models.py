from django.db import models

# Create your models here.

class Page(models.Model):
    title= models.CharField( max_length=50)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField()

    def __str__(self):
        return (self.title)

class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    

