from django.contrib import admin
from .models import *
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created')


class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'board', 'is_active', 'created')


class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'is_active', 'created',  'due_day')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('card', 'text', 'created')

admin.site.register(Board, BoardAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Comment, CommentAdmin)