from django.db import models
from django.utils import timezone
from datetime import timedelta

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def was_pub_recently(self, days=7):
        return self.pub_date >= timezone.now() - timedelta(days=days)

    def __str__(self):
        return "<问题：%s>" % self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "<%s: %s>" % (self.question, self.choice_text)
