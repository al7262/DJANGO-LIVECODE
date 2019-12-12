from django.shortcuts import render
from .models import Item

# Create your views here.

def index(request):
    items = Item.objects.all()
    return render(request, 'store/index.html', {
        'isHome': True,
        'items': items
    })

def detail(request, item_id):
    item = Item.object.get(pk=item_id)
    return render(request, 'store/detail.html', {
        'isHome': True,
        'item': item
    })