from django.shortcuts import render, redirect
from item.models import Category, Item
from .models import Cart, CartItem
from .forms import SignupForm
from django.http import JsonResponse
import json

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

def cart(request):
    
    cart = None
    cartItems = []
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartItems = cart.cartItems.all()
        
        # Calcola il prezzo totale per ogni elemento nel carrello
        for cartItem in cartItems:
            cartItem.total_price = cartItem.quantity * cartItem.item.price
    
    context = {'cart': cart, 'cartItems': cartItems}
    
    return render(request, 'core/cart.html', context)

def addToCart(request):
    data = json.loads(request.body)
    item_id = data['id']
    item = Item.objects.get(id=item_id)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, item=item)
        cartitem.quantity += 1
        cartitem.save()
        print(cartitem)
    
    return JsonResponse("Item was added", safe=False)