from django.db import models
from django.conf import settings


class Question(models.Model):
    """Define question database"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # as we defined it in settings
        on_delete=models.CASCADE,
        related_name="questions"
    )

    def __str__(self) -> str:
        return self.content


class Answer(models.Model):
    """Define Answer Model database"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="answers")
    voters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="votes")

    def __str__(self) -> str:
        return self.author.username
