from django.contrib import admin
from blog.models import Post
from blog.models import PostCategory

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)