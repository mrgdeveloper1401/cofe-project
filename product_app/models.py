from django.db import models
from treebeard.mp_tree import MP_Node
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _
from core_app.models import CreateMixin, UpdateMixin


class Category(MP_Node, CreateMixin, UpdateMixin):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey("core_app.Image", verbose_name=_("image"), on_delete=models.PROTECT, related_name="category_images")
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "product_category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Vendor(CreateMixin, UpdateMixin):
    user = models.OneToOneField("account_app.User", on_delete=models.PROTECT)
    shop_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    logo = models.ForeignKey("core_app.Image", verbose_name=_("image"), on_delete=models.PROTECT, related_name="vendor_images")
    is_active = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    class Meta:
        ordering = ("-id",)
        db_table = "vendor"


class Product(CreateMixin, UpdateMixin):
    TYPE_CHOICES = [
        ("normal", "عادی"),
        ("bestseller", "پرفروش"),
        ("amazing", "شگفت‌انگیز"),
        ("new", "جدید"),
    ]

    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, related_name="vendor_products")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name="category_products")

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    product_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="normal")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    new_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_installment = models.BooleanField(default=False)

    class Meta:
        ordering = ("-id",)
        db_table = "product"


class Attribute(CreateMixin, UpdateMixin):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "attribute"


class AttributeValue(CreateMixin, UpdateMixin):
    attribute = models.ForeignKey("Attribute", verbose_name=_("attribute"), on_delete=models.PROTECT)
    value = models.CharField(max_length=255)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "attribute_value"


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="attributes")
    attribute_value = models.ForeignKey("AttributeValue", verbose_name=_("attribute value"), on_delete=models.PROTECT)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "product_attribute_values"


class ProductMedia(models.Model):
    MEDIA_TYPE = [
        ("image", "تصویر"),
        ("video", "ویدیو"),
    ]
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="media")
    product_file = models.FileField(upload_to="product_media/")
    product_type = models.CharField(max_length=10, choices=MEDIA_TYPE)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "product_media"


class Installment(CreateMixin, UpdateMixin):
    order = models.ForeignKey("order_app.Order", on_delete=models.PROTECT, related_name="product_installments")
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = 'installment'


class Inventory(CreateMixin, UpdateMixin):
    product = models.OneToOneField('Product', on_delete=models.PROTECT, related_name="product_inventory")
    quantity = models.PositiveIntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=5)

    class Meta:
        db_table = "inventory"
        ordering = ("-id",)
