from django.db import models
from datetime import timedelta
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_pub_recently(self):
        return self.publish_date > timezone.now() - timedelta(days=7)


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
