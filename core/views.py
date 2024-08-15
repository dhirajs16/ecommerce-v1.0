from django.shortcuts import render
from item.models import Item

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[:4]
    # print(items)
    return render(request, 'core/index.html', {'items':items})


def contacts(request):
    return render(request, 'core/contacts.html')