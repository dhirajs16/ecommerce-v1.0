from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm
from .models import Item, Category
from django.db.models import Q



# Create your views here.

# browse items view
def items(request):
    categories = Category.objects.all().order_by('name')
    items = Item.objects.filter(is_sold = False).order_by('name')
    query = request.GET.get('query','')
    # print(query)
    if query:
        items = Item.objects.filter(
            Q(name__icontains = query) |
            Q(description__icontains = query) |
            Q(category__name__icontains = query)|
            Q(created_by__username__icontains = query)
        )

    return render(request, 'item/browse.html', {'items':items, 'categories': categories, 'query': query}) 


# deatiled item view
def detail(request, pk):
    item = get_object_or_404(Item, pk = pk)
    related_items = Item.objects.filter(category = item.category, is_sold = False).exclude(pk = pk)
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})


# create new item view
@login_required
def new_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk = item.id)
    else:
        form = NewItemForm()
    return render(request, 'item/new_item.html', {'form': form})


# update an item view
@login_required
def update_item(request, pk):
    item = get_object_or_404(Item, pk = pk)
    if request.method == "POST":
        form = NewItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk = item.pk)
    else:
        form = NewItemForm(instance = item)
    return render(request, 'item/update_item.html', {'form': form, 'item': item})


# delete view
@login_required
def delete_item(request, pk):
    Item.objects.filter(pk = pk).delete()
    return redirect('core:index')
    






