from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from Kanban.forms import CustomUserCreationForm
from .models import *


# Create your views here.

def dashboard(request):

    id = request.GET.get('id', 1)
    boards = Board.objects.filter(user=request.user)

    active_board = boards.get(id=id)
    lists = List.objects.filter(board=active_board)
    cards = Card.objects.all()
    return render(request, 'dashboard.html', {
        'boards': boards,
        'lists': lists,
        'cards': cards
    })


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")


def main(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return redirect("login")
