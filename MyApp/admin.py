from django.contrib import admin
from MyApp.models import Tweets, Followers, TweetLikes


@admin.register(Tweets)
class TweetsAdmin(admin.ModelAdmin):
    list_display = ("user","tweet_body",'created_date')


@admin.register(Followers)
class FollowersAdmin(admin.ModelAdmin):
    list_display = ("user","follower")


@admin.register(TweetLikes)
class TweetLikesAdmin(admin.ModelAdmin):
    list_display = ("tweet","like_by")