from django.db import models
from core_app.models import CreateMixin, UpdateMixin


class SupportTicket(CreateMixin, UpdateMixin):
    STATUS_CHOICES = [
        ("open", "باز"),
        ("in_progress", "در حال بررسی"),
        ("closed", "بسته‌شده"),
    ]

    user = models.ForeignKey("account_app.User", on_delete=models.PROTECT, related_name="user_tickets")
    subject = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")

    class Meta:
        db_table = "support_ticket"
        ordering = ("-id",)


class TicketMessage(CreateMixin, UpdateMixin):
    ticket = models.ForeignKey(SupportTicket, on_delete=models.PROTECT, related_name="messages")
    sender = models.ForeignKey("account_app.User", on_delete=models.PROTECT)
    message = models.TextField()
    is_staff = models.BooleanField(default=False)

    class Meta:
        db_table = "ticket_message"
        ordering = ("-id",)
