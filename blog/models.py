from django.db import models
from django.utils import timezone

class Contents(models.Model):
    title = models.CharField(max_length=20)
    word_text = models.CharField(max_length=140)
    date_time = models.DateTimeField('投稿日')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
