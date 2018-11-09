from django.db import models

class Userdb(models.Model):
    username = models.CharField(max_length=20)
    salt = models.CharField(max_length=8)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
