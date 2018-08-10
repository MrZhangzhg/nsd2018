from django.db import models
from datetime import timedelta
from django.utils import timezone

class Question(models.Model):
    'django将自动在数据库表中创建一个名为id的字段作为主键'
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish date')

    def was_published_recently(self):
        '判断问题是否是一天内发布的'
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    'django将自动在数据库表中创建一个名为id的字段作为主键'
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # 外键约束，django自动创建一个名为question_id的字段与polls_question
    # 表的id建立关系
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
# model编写完成后，需要执行以下语句
# python manage.py makemigrations
# python manage.py migrate
# 查看django生成的表，则：
# sqlite3 db.sqlite3
# sqlite> .tables
# sqlite> .schema polls_question

