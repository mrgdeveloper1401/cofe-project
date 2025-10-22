from django.db import models
from core_app.models import CreateMixin, UpdateMixin


class Wallet(CreateMixin, UpdateMixin):
    user = models.OneToOneField("account_app.User", on_delete=models.PROTECT, related_name="user_wallet")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = "wallet"
        ordering = ("-id",)


class WalletTransaction(CreateMixin, UpdateMixin):
    TRANSACTION_TYPES = (
        ('deposit', 'واریز'),
        ('withdraw', 'برداشت'),
        ('purchase', 'خرید'),
        ('refund', 'عودت'),
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='wallet_transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("-id",)
        db_table = "wallet_transaction"
