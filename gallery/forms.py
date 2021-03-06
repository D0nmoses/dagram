from django import forms
from .models import Post, Comment


class NewPostForm(forms.ModelForm):
    '''	
    Class to create a form for an authenticated user to create Post	
    '''
    class Meta:
        model = Post
        exclude = ['user','profile', 'post_date', 'tags']


class NewCommentForm(forms.ModelForm):
    '''	
    Class to create a form for an authenticated user to submit a comment	
    '''
    class Meta:
        model = Comment
        exclude = ['user', 'post']