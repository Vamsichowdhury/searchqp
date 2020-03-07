
from django.urls import path
from tweets import views
app_name = 'tweets'
urlpatterns = [

    path('mytweets/', views.tweet, name='tweets_list'),
    path("tweetsDelete/<int:pk>", views.deleteTweets, name='delete_tweets'),
    path("tweetCreateForm/", views.TweetForm.as_view(), name='tweetCreateForm'),

]
