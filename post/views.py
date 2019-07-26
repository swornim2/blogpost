from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView
from .models import Post



class HomeView(TemplateView):
    template_name = "home.html"


class BlogListView(ListView):
    template_name = "list.html"
    model = Post


class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = "create.html"
    model=Post
    fields=('title','description','image','is_published')
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()

        return super().form_valid(form)


    def get_success_url(self):
        messages.success(self.request, 'new blog has been posted successfully')
        return reverse("form")

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/signin.html"

    def get_success_url(self):
        messages.success(self.request, 'your account has been created successfully')
        return reverse("login")


class PostDetail(DetailView):
    model = Post
    template_name = "details.html"
    context_object_name = "obj"


class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "edit.html"
    fields=('title','description','image','is_published')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.creator != self.request.user:
            raise PermissionDenied("YOU HAVE NO RIGHT TO UPDATE")
        return obj

    def get_success_url(self):
        messages.success(self.request, 'post has been upadted successfully')
        return reverse("detail", args=(self.object.pk,))