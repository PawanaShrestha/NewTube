from tkinter import Widget
from turtle import width
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from newtubeapp.models import Profile

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'input-class', 'required': 'True', 'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'class': 'input-class', 'required': 'True', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'class': 'input-class', 'required': 'True', 'placeholder': 'Last Name' }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *arg, **kwargs):
        super(RegisterUserForm, self).__init__(*arg, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input-class'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'input-class'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        
        self.fields['password2'].widget.attrs['class'] = 'input-class'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''

        self.fields['email'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['username'].label = ''

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']   

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-input'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-input'})
        self.fields['email'].widget.attrs.update({'class': 'form-input'})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_dp']
    
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fields['bio'].widget.attrs.update({'class': 'form-input bio-input'})
        self.fields['profile_dp'].widget.attrs.update({'class': ' form-input'})

    
        
        
