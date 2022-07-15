from django.contrib import admin
from .models import Post, Tag

# Register your models here.

class PuslapisAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(Post, PuslapisAdmin)
admin.site.register(Tag)

