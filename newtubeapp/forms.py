from django import forms
from django.forms import ModelForm
from .models import Post

#Create a new video upload form

class UploadNewVideoForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'video', 'thumbnail', 'description', 'hashtags')

    def __init__(self, *arg, **kwargs):
        super(UploadNewVideoForm, self).__init__(*arg, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'title'
        self.fields['video'].widget.attrs['class'] = 'video'
        self.fields['thumbnail'].widget.attrs['class'] = 'thumbnail'
        self.fields['description'].widget.attrs['class'] = 'desc'
        self.fields['hashtags'].widget.attrs['class'] = 'hashtags'
        
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['hashtags'].widget.attrs['placeholder'] = 'Hashtags'

        self.fields['title'].label = ''
        self.fields['description'].label = ''