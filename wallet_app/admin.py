from django.contrib import admin
from .models import (
    Wallet,
    WalletTransaction
)


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass


@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):
    pass
