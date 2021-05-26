from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from Kanban.forms import CustomUserCreationForm
from .models import *


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
            return redirect("kanban")


def main(request):
    if request.user.is_authenticated:
        return redirect("kanban")
    else:
        return redirect("login")

def kanban(request):

    id = request.GET.get('id', 1)
    boards = Board.objects.filter(user=request.user)

    active_board = boards.get(id=id)
    lists = List.objects.filter(board=active_board)

    cards_in_lists = {}
    for card in Card.objects.all():
        if card.list.id in cards_in_lists:
            cards_in_lists[card.list.id].append(card)
        else:
            cards_in_lists[card.list.id] = [card]
    print(cards_in_lists[1])

    return render(request, 'kanban.html', {
        'boards': boards,
        'lists': lists,
        'cards': cards_in_lists
    })

    