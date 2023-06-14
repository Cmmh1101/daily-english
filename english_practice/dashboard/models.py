from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class FlashcardSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.topic

class Flashcard(models.Model):
    set = models.ForeignKey(FlashcardSet, on_delete=models.CASCADE)
    word_or_phrase = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.word_or_phrase} word in {self.set}"