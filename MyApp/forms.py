from django import forms
from MyApp.models import Tweets, Followers, TweetLikes
  

class NewTweetForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ['user','tweet_body']


class FollowersForm(forms.ModelForm):
    class Meta:
        model = Followers
        fields = ['user','follower']
        

class TweetLikesForm(forms.ModelForm):
    class Meta:
        model = TweetLikes
        fields = ['tweet','like_by']