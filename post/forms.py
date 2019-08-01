from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "creator",
            "description",
            "image",
            "is_published",
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = (
            "name",
            "email",
            "comment"

        )
  