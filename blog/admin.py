from django.contrib import admin

# Register your models here. Pasting from djangogirls tutorial
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)