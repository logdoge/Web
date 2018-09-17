from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    votes = models.IntegerField()
    def __str__(self):
        return self.choice