from django.shortcuts import redirect
from Kanban.views import register, main, kanban, card_info, card_update
from django.urls import path
# from .views import register, login, reset, forgot
urlpatterns = [
    path('', main),
    path('register/', register),
    path('kanban/', kanban, name="kanban"),
    path('card_info/<int:card_id>', card_info, name="card_info"),
    path('card_update/<int:card_id>', card_update),
    path('card_update/', main),

    


]
