from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']  # Removed 'user' field as it should be set in the view
        