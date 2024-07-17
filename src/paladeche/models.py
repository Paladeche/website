from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
