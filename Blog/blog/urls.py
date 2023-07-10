from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostListView, PostDetailView, PostFormView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostFormView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostFormView.as_view(), name='post_edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)