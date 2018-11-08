from django.db import models
from datetime import timedelta
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def was_publish_recently(self, days=7):
        return self.pub_date > timezone.now() - timedelta(days=days)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.question, self.choice_text)
