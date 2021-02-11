from django.contrib import admin
from .models import Course, OrderItem, Order, Address, Lesson, Reviews, CourseMeta

# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Reviews)
admin.site.register(Address)
admin.site.register(CourseMeta)
