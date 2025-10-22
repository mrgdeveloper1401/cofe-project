from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator
from core_app.models import CreateMixin, UpdateMixin


class Order(CreateMixin, UpdateMixin):
    reserved_until = models.DateTimeField(blank=True)
    first_name = models.CharField(_("نام سفارش دهنده"))
    is_reserved = models.BooleanField(default=False)
    last_name = models.CharField(_("نام خوانوادگی سفارش دهنده"))
    phone = models.CharField(_("شماره تماس سفارش دهنده"), max_length=15)
    description = models.CharField(max_length=500, blank=True, null=True)
    STATUS_CHOICES = [
        ('pending', 'در انتظار پرداخت'),
        ('paid', 'پرداخت شده'),
        # ('processing', 'در حال پردازش'),
        # ('shipped', 'ارسال شده'),
        # ('delivered', 'تحویل داده شده'),
        ('cancelled', 'لغو شده'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(
        "account_app.User",
        on_delete=models.PROTECT,
        related_name="user_orders",
    )
    is_complete = models.BooleanField(default=False)
    address = models.ForeignKey(
        "account_app.UserAddress",
        related_name="user_order_address",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    tracking_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    shipping = models.ForeignKey(
        "ShippingMethod",
        on_delete=models.PROTECT,
        related_name="order_shipping_methods",
        blank=True, # TODO, when clean migration we remove field blank and null
        null=True
    )
    is_active = models.BooleanField(default=True)
    # items_data = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ("-id",)
        db_table = "orders"


class OrderItem(CreateMixin, UpdateMixin):
    order = models.ForeignKey(
        "Order",
        on_delete=models.PROTECT,
        related_name="order_items",
    )
    product = models.ForeignKey(
        "product_app.Product",
        on_delete=models.PROTECT,
        related_name="product_order_items",
    )
    price = models.DecimalField(max_digits=12, decimal_places=3)
    quantity = models.PositiveIntegerField(
        default=1,
        validators=(MinValueValidator(1),),
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "order_item"


class ShippingCompany(CreateMixin, UpdateMixin):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "shipping_company"


class ShippingMethod(CreateMixin, UpdateMixin):
    class ShippingType(models.TextChoices):
        STANDARD = "standard", _("پست معمولی")
        EXPRESS = "express", _("پست پیشتاز")
        FREE = "free", _("ارسال رایگان")

    company = models.ForeignKey(
        ShippingCompany,
        on_delete=models.PROTECT,
        related_name="methods",
        verbose_name=_("شرکت ارسال‌کننده")
    )
    name = models.CharField(_("نام روش ارسال"), max_length=100)
    shipping_type = models.CharField(
        _("نوع ارسال"),
        max_length=20,
        choices=ShippingType.choices,
        default=ShippingType.STANDARD
    )
    price = models.DecimalField(
        _("هزینه ارسال"),
        max_digits=10,
        decimal_places=2
    )
    estimated_days = models.PositiveIntegerField(_("تعداد روزهای تخمینی تحویل"))
    is_active = models.BooleanField(_("فعال"), default=True)

    class Meta:
        db_table = "shipping_method"
        ordering = ("-id",)
