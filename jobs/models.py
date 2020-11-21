from django.db import models

# Create your models here.

class job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/')
    summary = models.TextField(max_length= 5000)
    
    def __str__(self):              #It will change blog name to the title of it in the database
        return self.title