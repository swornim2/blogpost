from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Post


class HomeView(TemplateView):
    template_name = "home.html"


class BlogListView(ListView):
    template_name = "list.html"
    model = Post


class BlogCreateView(CreateView):
    template_name="create.html"
    model=Post
    fields=('title','description','image','is_published','creator')

    def get_success_url(self):
        messages.success(self.request, 'new blog has been posted successfully')
        return reverse("form")

