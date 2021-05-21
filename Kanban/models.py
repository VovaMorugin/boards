from django.db import models
from django.contrib.auth import get_user_model
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