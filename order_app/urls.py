from django.urls import path

from .views import ShoppingView, PaymentView, UnsuccessflyPaymentView

app_name = "order_app"

urlpatterns = [
    path("shopping/", ShoppingView.as_view(), name="shopping"),
    path("payment/", PaymentView.as_view(), name='payment'),
    path("unsuccess/", UnsuccessflyPaymentView.as_view(), name='unsuccess-payment')
]
