from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "creator",
            "description",
            "image",
            "total_comments",
            "is_published",
        )

