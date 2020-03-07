from django.shortcuts import render, redirect, HttpResponse
from .models import Tweets
from django.views.generic import CreateView
from .forms import TweetForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def tweet(request):
    tweets = Tweets.objects.all()
    return render(request, 'tweets/mytweets.html', {'tweets': tweets})


class TweetForm(LoginRequiredMixin, CreateView):
    model = Tweets
    form_class = TweetForm
    template_name = 'tweets/tweetForm.html'
    context_object_name = 'form'
    success_url = reverse_lazy('tweets:tweets_list')

    def form_valid(self, TweetForm):
        TweetForm.instance.author = self.request.user
        return super().form_valid(TweetForm)


def deleteTweets(request, pk):
    tweet = Tweets.objects.get(pk=pk)
    if request.user == tweet.author:
        Tweets.objects.filter(id=pk).delete()
        messages.success(request, f'tweet is deleted')
        return redirect('/tweets/mytweets/')

    else:
        messages.warning(request, f'you cannot have access to delete this tweet')
        return redirect('/tweets/mytweets/')
