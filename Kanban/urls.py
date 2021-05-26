from Kanban.views import register, main, kanban
from django.urls import path
# from .views import register, login, reset, forgot
urlpatterns = [
    path('', main),
    path('register/', register),
    path('kanban/', kanban, name="kanban")
]