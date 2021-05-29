from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from .models import Card, List, Board


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ['user']

        fields = [
            'list',
            'title',
            'description'
        ]


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = [
            
            'title',
            'board',
        ]


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = [
            'title',
        ]
