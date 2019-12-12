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

def new(request):
    return render(request, 'store/new.html', {
        'isHome': True
    })

def posted(request):
    toItem = Item()
    toItem.name = request.POST['name']
    toItem.photo = request.POST['photo']
    toItem.price = request.POST['price']
    toItem.detail = request.POST['detail']
    toItem.save()
    items = Item.objects.all()
    return render(request, 'store/index.html', {
        'isHome': True,
        'items': items
    })