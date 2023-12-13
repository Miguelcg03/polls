from django.db import models
from polls.models import Poll
from choices.models import Choice
# Create your models here.
class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)  # Utilizo auto_now_add para registrar la fecha y hora en que se votó

    def __str__(self):
        return f'Vote for {self.choice} in {self.poll} at {self.voted_at}'