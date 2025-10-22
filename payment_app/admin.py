from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db.models import JSONField
from .models import (
    Payment,
    PaymentGateWay,
    ResultPaymentGateWay
)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentGateWay)
class PaymentGateWayAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(ResultPaymentGateWay)
class ResultPaymentGateWayAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
