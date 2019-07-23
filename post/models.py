from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    TYPE_CHOICES = (('private', 'Private'), ('public', 'Public'))
    title = models.CharField(max_length=200, verbose_name="Post Title", )
    description = models.TextField(help_text="Description")
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='post/images', null=True, blank=True)
    total_comments = models.IntegerField(default=0)
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default='public')
    is_published = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        ordering = ['-created_date', '-modified_date']
        verbose_name = "BlogPost"

    def __str__(self):
        return self.title


class Comment(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        ordering = ['-created_date', '-modified_date']

    def __str__(self):
        return self.user.first_name if self.user else self.name


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'creator', 'image', 'type']


