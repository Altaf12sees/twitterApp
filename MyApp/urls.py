from django.contrib.auth import views as auth_views
from . import views
from django.urls import path


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create_tweets/', views.create_tweets, name='create_tweets'),
    path('add_followers/', views.add_followers, name='add_followers'),
    path('save_tweet_likes/', views.save_tweet_likes, name='save_tweet_likes'),
    path('get_liked_tweets/', views.get_liked_tweets, name='get_liked_tweets'),
    path('search_tweets/', views.search_tweets, name='search_tweets'),
]