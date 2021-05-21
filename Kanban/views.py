from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from Kanban.forms import CustomUserCreationForm


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

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