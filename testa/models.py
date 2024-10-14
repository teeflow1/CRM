from django.db import models

class List(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    fjuff
    
    
    def __str__(self):
        return(f"{self.first_name}{self.last_name}")
    
