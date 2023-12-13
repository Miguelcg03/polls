from django.db import models
from polls.models import Poll
# Create your models here.
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name