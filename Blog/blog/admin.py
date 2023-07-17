from django.contrib import admin
from blog.models import Post
from blog.forms import PostForm

class PostFormAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Post, PostFormAdmin)
