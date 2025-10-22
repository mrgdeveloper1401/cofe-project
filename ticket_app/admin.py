from django.contrib import admin
from .models import (
    SupportTicket,
    TicketMessage
)


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    pass


@admin.register(TicketMessage)
class TicketMessageAdmin(admin.ModelAdmin):
    pass
