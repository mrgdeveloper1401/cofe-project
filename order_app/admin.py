from django.contrib import admin
from .models import (
    Order,
    OrderItem,
    ShippingCompany,
    ShippingMethod
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ShippingCompany)
class Admin(admin.ModelAdmin):
    pass


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    pass
