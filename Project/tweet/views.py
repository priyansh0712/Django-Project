from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

def testing(request):
    return render(request,'index.html')

def dispay_tweet(request):
    tweets = Tweet.objects.all().order_by('-date')
    return render(request,'tweet_list.html',{'tweet': tweets})

def create_tweet(request):
    form = None
    if request.method == 'POST':
        form = TweetForm(request.POST , request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('display_tweet')
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})

def edit_tweet(request , tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id , user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST , request.FILES , instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('display_tweet')
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

def delete_tweet(request , tweet_id):
    tweet = get_object_or_404(Tweet , pk = tweet_id , user = request.user)
    if request.method == 'POST':
        Tweet.delete()
        return redirect('display_tweet')
    return render(request,'tweet_delete.html',{'tweet':tweet})
