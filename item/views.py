from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm
from .models import Item, Category



# Create your views here.
def items(request):
    categories = Category.objects.all().order_by('name')
    items = Item.objects.filter(is_sold = False).order_by('name')
    # if request.method == 'GET':
    #     search_value = request.GET.get('search')
    #     print(search_value)
    #     items = Item.objects.filter(is_sold = False, name__icontains = search_value)
    #     return redirect('item:items')
    
    return render(request, 'item/browse.html', {'items':items, 'categories': categories}) 



def detail(request, pk):
    item = get_object_or_404(Item, pk = pk)
    related_items = Item.objects.filter(category = item.category, is_sold = False).exclude(pk = pk)
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})

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


@login_required
def delete_item(request, pk):
    Item.objects.filter(pk = pk).delete()
    return redirect('core:index')
    






