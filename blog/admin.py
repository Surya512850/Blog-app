from django.contrib import admin
from .models import Post,PreviousPost
# Register your models here
admin.site.register(Post)
admin.site.register(PreviousPost)