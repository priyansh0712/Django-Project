from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

# View for Display all Tweet 
def dispay_tweet(request):
    tweets = Tweet.objects.all().order_by('-date')
    return render(request,'tweet_list.html',{'tweet': tweets})

# View for Create Tweet
@login_required
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
            print(form.errors)
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})

# View for Edit Tweet
@login_required
def edit_tweet(request , tweet_id):
    # Get the tweet object or return 404 if not found, ensuring user owns the tweet
    tweet = get_object_or_404(Tweet,pk = tweet_id , user = request.user)
    if request.method == 'POST':
        # Create form with POST data and files, binding to existing tweet instance
        form = TweetForm(request.POST , request.FILES , instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('display_tweet')
    else:
        # Create form pre-populated with existing tweet data
        form = TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

# View for Delete Tweet
@login_required
def delete_tweet(request , tweet_id):
    tweet = get_object_or_404(Tweet , pk = tweet_id , user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('display_tweet')
    return render(request,'tweet_delete.html',{'tweet':tweet})
