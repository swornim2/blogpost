from django.urls import path
from .views import HomeView, BlogListView, BlogCreateView


urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
    path('list/', BlogListView.as_view(), name="list"),
    path('form/', BlogCreateView.as_view(), name="form"),

]
