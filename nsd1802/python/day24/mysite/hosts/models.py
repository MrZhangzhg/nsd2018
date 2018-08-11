from django.db import models

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ip_addr = models.CharField(max_length=15)
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.hostname
