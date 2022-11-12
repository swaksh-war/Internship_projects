from django.db import models
# Create your models here.
class Criminal(models.Model):
    
    name = models.CharField(max_length=27)
    image = models.FileField(upload_to='criminal',null=True)
    location = models.TextField(null=True,max_length=200)
    pnum = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)
