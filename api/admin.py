from django.contrib import admin
from api.models import User, Address, Brand, Category, Product, ProductImage,\
                       Supplier, Order, OrderItem, CartItem, Wishlist, Review, \
                       Comment, Deal

admin.site.register(User)

admin.site.register(Address)

admin.site.register(Brand)

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "stock")

admin.site.register(ProductImage)

admin.site.register(Review)

admin.site.register(Supplier)