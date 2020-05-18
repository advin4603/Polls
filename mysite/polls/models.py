from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    publisher = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default='admin')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text


