from django.contrib import admin
from .models import Post 

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'public', 'status')
    date_hierarchy = 'public'
    raw_id_fields = ('author', )
    list_filter = ('status', 'created', 'public', 'author')
    search_fields = ('title', 'data')
    prepopulated_fields = {'slug': ('title', )}
# Register your models here.
