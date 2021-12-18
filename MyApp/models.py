from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Tweets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user = models.CharField(max_length=50)
    tweet_body = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.tweet_body)

class Followers(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    follower = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user.id)


class TweetLikes(models.Model):
    tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    like_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    

