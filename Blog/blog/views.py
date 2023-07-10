from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    """Контроллер для рендеринга страницы списка постов"""
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    return render(request=request, template_name='blog/post_list.html', context={'posts':posts})

def post_detail(request, pk):
    """Контроллер для рендеринга одного поста"""
    print(pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request=request, template_name='blog/post_detail.html', context={'post':post})
    
def post_new(request):
    """Контроллер для формы создания поста"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect(to='post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request=request, template_name='blog/post_edit.html', context={'form':form})

def post_edit(request, pk):
    """Контроллер для формы редактирования поста"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect(to='post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request=request, template_name='blog/post_edit.html', context={'form':form})
