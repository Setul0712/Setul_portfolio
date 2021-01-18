from django.db import models
from django.utils.safestring import mark_safe

# Create your models here

class blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField(auto_now=False, auto_now_add=False)
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')


def save(self, *args, **kwargs):
    self.text_field = mark_safe(self.text_field.replace("\n", "<br/>"))
    super(YourModel, self).save(*args, **kwargs)
    def __str__(self):              #It will change blog name to the title of it in the database
        return self.title

    def pub_date_done(self):        #Changing the date form it was not good so..
       return self.pub_date.strftime('%b %e %Y')

   # def summary(self):
   #     return self.body[:100]
   
   
