from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count, Max
from django.conf import settings
from blog.forms import PostForm
from blog.models import Post
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s %(message)s]')
logger = logging.getLogger(__name__)


class PostListView(ListView):
    """Класс контроллер для отображения списка постов"""
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        if not self.request.user.is_authenticated and settings.LOG_USER:
            meta = self.request.META
            method_request = meta.get('REQUEST_METHOD')
            url = f"{meta.get('PATH_INFO')}"
            ip = meta.get('REMOTE_ADDR')
            logger.info(f'IP: {ip} URL: {url} TYPE: {method_request}')
        
        return queryset.filter(published_at__lte=timezone.now()).order_by('-published_at')


class AuthorListView(ListView):
    """Класс контроллер для отображения списка авторов"""
    model = Post
    queryset = dict()
    queryset['posts'] = Post.objects.values('author')\
        .annotate(sum_post=Count('author'), last_date=Max('created_at'))
    queryset['authors'] = User.objects.values('id', 'username')
    template_name = 'blog/authors_list.html'
    context_object_name = 'data'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated and settings.LOG_USER:
            meta = self.request.META
            method_request = meta.get('REQUEST_METHOD')
            url = f"{meta.get('PATH_INFO')}"
            ip = meta.get('REMOTE_ADDR')
            logger.info(f'IP: {ip} URL: {url} TYPE: {method_request}')
        return super().dispatch(request, *args, **kwargs)


class PostDetailView(DetailView):
    """Класс контроллер для отображения одного поста"""
    model = Post
    template_name = 'blog/post_detail.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated and settings.LOG_USER:
            meta = self.request.META
            method_request = meta.get('REQUEST_METHOD')
            url = f"{meta.get('PATH_INFO')}"
            ip = meta.get('REMOTE_ADDR')
            logger.info(f'IP: {ip} URL: {url} TYPE: {method_request}')
        return super().dispatch(request, *args, **kwargs)


class PostFormView(FormView):
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.kwargs.get('pk'):
            kwargs['instance'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return kwargs

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_at = timezone.now()
        post.save_img()
        post.save()
        return redirect(to='post_detail', pk=post.pk)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated and settings.LOG_USER:
            meta = self.request.META
            method_request = meta.get('REQUEST_METHOD')
            url = f"{meta.get('PATH_INFO')}"
            ip = meta.get('REMOTE_ADDR')
            logger.info(f'IP: {ip} URL: {url} TYPE: {method_request}')
        return super().dispatch(request, *args, **kwargs)
