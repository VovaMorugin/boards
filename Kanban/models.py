from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
# Create your models here.

User = get_user_model()


class Board(models.Model):
    class Meta:
        db_table = 'boards'
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'

    title = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class List(models.Model):
    class Meta:
        db_table = 'lists'
        verbose_name = 'List'
        verbose_name_plural = 'Lists'

    title = models.CharField(max_length=100, null=False, blank=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    class Meta:
        db_table = 'cards'
        verbose_name = 'card'
        verbose_name_plural = 'cards'

    list = models.ForeignKey(List, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    due_day = DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title

class Comment(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=False, blank=False)

def __str__(self):
    return self.card.title   