from django.db import models
from django.contrib.auth import get_user_model


class Tweets(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    tweet = models.CharField(max_length=100)

    def __str__(self):
        return self.tweet
