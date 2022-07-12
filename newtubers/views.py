import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from newtubeapp.models import Post, Profile
from newtubers.forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User

# LOGIN USER
def login_user(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There was an error logging in.'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


#LOGOUT USER
def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out Successfully."))
    return redirect('login')


#REGISTER USER
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Registration successful!"))
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form': form
        })


#USER PROFILE
def user_profile(request):
    users = User.objects.filter(username = request.user.username)
    posts = Post.objects.filter(uploader = request.user.username)
    return render(request, 'authenticate/profile.html', {
        'users': users,
        'posts': posts,
    })


#EDIT USER PROFILE
def edit_user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, ("Account updated!"))
            return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render (request, 'authenticate/edit_user_profile.html', context)

def profile_admin(request):
    user = Profile.objects.get(created_by=request.user)
    return render(request, 'authenticate/edit_user_profile.html', {'user': user})
    

    



