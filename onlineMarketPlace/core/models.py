from django.db import models    
from django.contrib.auth.models import User
import uuid

from item.models import Item

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='itemsCart')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartItems')
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.item.name