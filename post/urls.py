from django.urls import path
from .views import HomeView, BlogListView, BlogCreateView, SignUpView, PostDetail, PostEdit


urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
    path('post/list/', BlogListView.as_view(), name="list"),
    path('post/add/', BlogCreateView.as_view(), name="form"),
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    path("blog/<int:pk>/", PostDetail.as_view(), name="detail"),
    path("blog/<int:pk>/edit/", PostEdit.as_view(), name="edit"),



]
