from django.contrib import admin
from api.models import User, Address, Brand, Category, Product, ProductImage,\
                       Supplier, Order, OrderItem, CartItem, Wishlist, Review, \
                       Comment, Deal

admin.site.register(User)

admin.site.register(Address)

admin.site.register(Brand)

admin.site.register(Category)

admin.site.register(Product)

