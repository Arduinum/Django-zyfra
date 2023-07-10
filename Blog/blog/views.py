from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):
    """Класс контроллер для отображения списка постов"""
    model = Post
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published_at__lte=timezone.now()).order_by('-published_at')

class PostDetailView(DetailView):
    """Класс контроллер для отображения одного поста"""
    model = Post
    template_name = 'blog/post_detail.html'


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
        post.save()
        return redirect(to='post_detail', pk=post.pk)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
