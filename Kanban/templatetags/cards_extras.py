from django import template
from ..models import Card

register = template.Library()

@register.simple_tag
def cards_in_list(cards, list_id):
    return Card.objects.filter(list_id = list_id)

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')
