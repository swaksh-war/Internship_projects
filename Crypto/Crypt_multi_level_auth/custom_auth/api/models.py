from django.db import models

# Create your models here.
class Custom_auth(models.Model):
    user = models.CharField(max_length=200)
    auth_token = models.UUIDField()

    def __str__(self):
        return self.user
    
