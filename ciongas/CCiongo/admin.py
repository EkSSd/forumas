from django.contrib import admin
from .models import Puslapis, Tagg

# Register your models here.

class PuslapisAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(Puslapis, PuslapisAdmin)
admin.site.register(Tagg)

