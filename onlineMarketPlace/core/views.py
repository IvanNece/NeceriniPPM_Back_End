from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(isSold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    # Check if the form is submitted
    if request.method == 'POST':
        # Take all the data from the form and save it to the database
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
         form = SignupForm()
         
    return render(request, 'core/signup.html', {'form': form})