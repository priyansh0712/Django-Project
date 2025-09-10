from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm,UserForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

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

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('display_tweet')
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})

def about(request):
    return render(request,'about.html')

def contact(request):
    from django.core.mail import send_mail
    from django.conf import settings
    message_sent = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'Contact Form Submission from {name}'
        full_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        message_sent = True
    return render(request, 'contact.html', {'message_sent': message_sent})