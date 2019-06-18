from django.contrib import admin

# Register your models here.
from news_update.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on',)
    list_filter = ("status",)
    search_fields = ['title','contents']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)
