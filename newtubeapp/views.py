from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView
from urllib3 import get_host
from newtubeapp.forms import UploadNewVideoForm
from .models import Ads, Post
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here

def delete_post(request, post_id):
    post = Post.objects.get(pk = post_id)
    post.delete()
    return redirect('user_profile')


def update_post(request, post_id):
    post = Post.objects.get(pk = post_id)
    form = UploadNewVideoForm(request.POST or None, request.FILES or None, instance = post)
    if form.is_valid():
        form.save()
        return redirect('user_profile')
    return render(request, "update_post.html", {
        'post': post,
        'form': form,
    })


def search_videos(request):
    if request.method == "POST":
        searched = request.POST['searched']
        videos = Post.objects.filter(title__contains = searched)
        return render(request, "searches.html",
         {'searched': searched,
         'videos': videos})
        
    else:
        return render(request, "searches.html", {})


def HomeView(request):
    posts = Post.objects.all().order_by('?')
    ads = Ads.objects.all()
    return render (request, 'home.html', {
        'posts': posts,
        'ads': ads
    })

def upload_new_video(request):
    submitted = False
    if request.method == "POST":
        form = UploadNewVideoForm(request.POST, files = request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.uploader = request.user.username #logged in user
            if upload.uploader == None:
                upload.uploader = "admin"
            upload.save()
            return HttpResponseRedirect('/upload_new_video?submitted=True')
    else :
        form = UploadNewVideoForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'upload_new_video.html', {"form": form, 'submitted': submitted})

def play_video(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'playvideo.html', {'post' : post})

def users_profile(request, user_name):
    user = User.objects.filter(username = user_name)
    return render(request, 'users_profile.html', {'user': user})


