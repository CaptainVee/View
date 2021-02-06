from django.contrib import admin
from .models import Post, OrderItem, Order, Address, Lesson

# Register your models here.

admin.site.register(Post)
admin.site.register(Lesson)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Address)
