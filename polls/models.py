from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=True)  # Cambié el campo a BooleanField para representar el estado activo/inactivo
    opened_from = models.DateTimeField()
    opened_to = models.DateTimeField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'Poll {self.name}'