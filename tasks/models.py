from django.db import models
from django.conf import settings
# Create your models here.
class Task(models.Model):

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  class Status(models.TextChoices):
    PENDING = "pending", "Pending"
    COMPLETED = "completed", "completed"

  title = models.CharField(max_length=200)
  description = models.CharField(max_length=400)

  status = models.CharField(
    max_length=40,
    choices=Status.choices,
    default=Status.PENDING
  )

  def __str__(self):
    return self.title