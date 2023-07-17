from django import forms
from blog.models import Post
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    """Класс для создания формы для поста"""
    class Meta:
        model = Post
        fields = ('title', 'photo', 'text')
        widgets = {'text': TinyMCE(attrs={'cols': 80, 'rows': 30})}
