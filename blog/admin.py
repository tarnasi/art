from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = ('user', 'title', 'content', 'photo')
    list_display = ('user', 'title', 'created_at', 'photo')


admin.site.register(Post, PostAdmin)

