from django.db import models

class Message(models.Model):
    msg = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.msg
