from .models import Tweets
from django import forms


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ['tweet']
