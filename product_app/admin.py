from django.contrib import admin
from .models import (
    Category,
    Vendor,
    Product,
    ProductAttributeValue,
    ProductMedia,
    Attribute,
    AttributeValue,
    Installment,
    Inventory
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductMedia)
class ProductMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass
