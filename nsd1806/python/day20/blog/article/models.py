from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title
