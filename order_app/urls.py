from django.urls import path

from .views import (
    ShoppingView, 
    PaymentView, 
    UnsuccessflyPaymentView,
    SuccessfltView
    )

app_name = "order_app"

urlpatterns = [
    path("shopping/", ShoppingView.as_view(), name="shopping"),
    path("payment/", PaymentView.as_view(), name='payment'),
    path("unsuccess/", UnsuccessflyPaymentView.as_view(), name='unsuccess-payment'),
    path("successfly/", SuccessfltView.as_view(), name='successfly_payment')
]
