from Kanban.views import dashboard, register, main
from django.urls import path
# from .views import register, login, reset, forgot
urlpatterns = [
    path('', main),
    path('dashboard/', dashboard, name="dashboard"),
    path('register/', register)
]