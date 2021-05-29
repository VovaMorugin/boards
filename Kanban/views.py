from django.contrib.auth import login
from django.shortcuts import redirect, render
from Kanban.forms import CustomUserCreationForm
from .models import *
from .forms import CardForm, BoardForm, ListForm


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

    card_form = CardForm(request.POST or None)
    if card_form.is_valid():
        card_form.save()
        return redirect("kanban")

    if request.method == 'GET' and 'del_card_id' in request.GET:
        card_id = request.GET.get('del_card_id', None)
        Card.objects.get(id=card_id).delete()
        return redirect("kanban")

    active_board = boards.get(id=id)
    lists = List.objects.filter(board=active_board)

    cards_in_lists = {}
    for card in Card.objects.all():
        if card.list.id in cards_in_lists:
            cards_in_lists[card.list.id].append(card)
        else:
            cards_in_lists[card.list.id] = [card]

    return render(request, 'kanban.html', {
        'boards': boards,
        'lists': lists,
        'cards': cards_in_lists,
        'card_form': card_form,
    })


def card_info(request, card_id):

    current_card = Card.objects.get(id=card_id)
    comments = Comment.objects.filter(card=current_card)
    context = {
        'current_card': current_card,
        'comments': comments
    }
    return render(request, 'card_info.html', context)


def card_update(request, card_id):
    current_card = Card.objects.get(id=card_id)
    update_form = CardForm(instance=current_card)
    if request.method == 'POST':
        update_form = CardForm(request.POST, instance=current_card)
        if update_form.is_valid():
            update_form.save()
            return redirect("kanban")

    context = {
        'update_form': update_form,
        'id': card_id
    }
    return render(request, 'card_update.html', context)
