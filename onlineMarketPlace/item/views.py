from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item, Category
from .forms import NewItemForm, EditItemForm

# Create your views here.
def items(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    categoryId = request.GET.get('category', 0)
    items = Item.objects.filter(isSold=False)
    
    if categoryId:
        items = items.filter(category_id=categoryId)
    
    if query:
        # i stays for case insensitive
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'categoryId': int(categoryId),
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    relatedItems = Item.objects.filter(category=item.category, isSold = False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html',{
        'item': item,
        'relatedItems': relatedItems,
    })
    
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Commit false because we need to add the owner first before saving
            item = form.save(commit=False)
            item.createdBy = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
        
        
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })
    
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, createdBy=request.user)
    item.delete()
    
    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, createdBy=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            # Commit false because we need to add the owner first before saving
            item = form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
        
        
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })
