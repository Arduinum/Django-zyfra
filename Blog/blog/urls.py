from django.urls import path
from blog.views import PostListView, PostDetailView, PostFormView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostFormView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostFormView.as_view(), name='post_edit')
]