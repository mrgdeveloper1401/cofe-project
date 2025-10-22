from django.db import models
from django.utils.translation import gettext_lazy as _
from core_app.models import CreateMixin, UpdateMixin


class Payment(CreateMixin, UpdateMixin):
    order = models.OneToOneField("order_app.Order", on_delete=models.PROTECT, related_name="order_payment")
    transaction_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, choices=[("pending", "در انتظار"), ("success", "موفق"), ("failed", "ناموفق")])
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    gateway = models.CharField(max_length=100, default="nowpayments")
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        db_table = "payment"
        ordering = ("-id",)


class PaymentGateWay(CreateMixin, UpdateMixin):
    order = models.ForeignKey(
        "order_app.Order",
        on_delete=models.PROTECT,
        related_name="payment_gateways",
    )
    user = models.ForeignKey("account_app.User", on_delete=models.PROTECT, related_name="gateways")
    payment_gateway = models.JSONField()
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "payment_gateway"


class ResultPaymentGateWay(CreateMixin, UpdateMixin):
    payment_gateway = models.ForeignKey(
        PaymentGateWay,
        on_delete=models.PROTECT,
        related_name="result_payment_gateways",
    )
    result = models.JSONField()
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "result_payment_gateway"
