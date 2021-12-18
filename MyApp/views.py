from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Tweets, Followers, TweetLikes
from django.urls import reverse
from .forms import *
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


# Home View
@login_required
def home(request):
    get_tweets = Tweets.objects.filter()
    get_followers_list = Followers.objects.filter()
    login_user = request.user
    users = get_user_model().objects.all()
    get_like_tweet_data = TweetLikes.objects.filter(like_by = login_user.id)

    return render(request, "registration/home.html",
        {'get_tweets':get_tweets,
        'login_user':login_user,
        'user_list':users,
        'get_followers_list':get_followers_list,
        'get_like_tweet_data':get_like_tweet_data})
 
 
 #Register a user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


#create new tweets
@login_required
def create_tweets(request):
    if request.method == 'POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user')
            tweet_body = form.cleaned_data.get('tweet_body')
            return redirect('home')
    else:
        form = NewTweetForm()
    login_user = request.user
    return render(request, 'tweetpages/create_tweets.html', {'form': form, 'login_user':login_user})


#add followers
@login_required
def add_followers(request):
    if request.method == 'POST':
        form = FollowersForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user')
            follower = form.cleaned_data.get('follower')
            return redirect('home')
    else:
        form = FollowersForm()
    login_user = request.user
    return render(request, 'registration/home.html', {'form': form, 'login_user':login_user})


#save tweet likes
@login_required
def save_tweet_likes(request):
    if request.method == 'POST':
        form = TweetLikesForm(request.POST)
        if form.is_valid():
            form.save()
            tweet = form.cleaned_data.get('tweet')
            like_by = form.cleaned_data.get('like_by')
            return redirect('home')
    else:
        form = TweetLikesForm()
    login_user = request.user
    return render(request, 'registration/home.html', {'form': form, 'login_user':login_user})


#Get all liked tweets
@login_required
def get_liked_tweets(request):
    login_user = request.user
    get_data = TweetLikes.objects.filter(like_by = login_user.id)
    return render(request, 'tweetpages/liked_tweets.html', {'login_user':login_user,'get_data':get_data})


#view for search tweet page
@login_required
def search_tweets(request):
    search_filter = request.GET.get('follower_filter')
    login_user = request.user
    get_followers_list = Followers.objects.filter(follower=login_user.id)
    try:
        users = get_user_model().objects.get(username = search_filter).pk
        get_filter_tweets = Tweets.objects.filter(user = users)
        
        return render(request, 'tweetpages/search_tweets.html',
            {'login_user':login_user,
            'get_filter_tweets':get_filter_tweets, 
            'get_followers_list':get_followers_list,
            'search_filter':search_filter})
    except ObjectDoesNotExist:
        return render(request, 'tweetpages/search_tweets.html',{'get_followers_list':get_followers_list})

    
