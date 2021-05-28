from Kanban.views import register, main, kanban, card_create_view, card_info
from django.urls import path
# from .views import register, login, reset, forgot
urlpatterns = [
    path('', main),
    path('register/', register),
    path('kanban/', kanban, name="kanban"),
    path('card/', card_create_view, name="new_card"),
    path('card_info/<int:card_id>', card_info, name="card_info")


]
