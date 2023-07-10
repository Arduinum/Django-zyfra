from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    """Класс для создания формы для поста"""
    class Meta:
        model = Post
        fields = ('title', 'photo', 'text')
