from datetime import timedelta
from django.utils import timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField()

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, models.CASCADE)

    def __str__(self):
        return "%s-> %s" % (self.choice_text, self.votes)
