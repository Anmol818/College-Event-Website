from django.db import models

# Create your models here.

class CollegeEvent(models.Model):
    event_id = models.AutoField
    event_name = models.CharField(max_length=200)
    event_date = models.DateField((""), auto_now=False, auto_now_add=False)
    event_time = models.TimeField()
    event_description = models.CharField(max_length=1000, default="")
    event_price= models.IntegerField(default=0)
    event_image = models.ImageField(upload_to="events/images", default="")
    
    def __str__(self):
        return self.event_name

    

