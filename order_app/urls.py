from django.urls import path

from .views import (
    ShoppingView, 
    PaymentView, 
    UnsuccessflyPaymentView,
    SuccessfltView,
    ShoppingCartView,
    CartEmptyView
    )

app_name = "order_app"

urlpatterns = [
    path("shopping/", ShoppingView.as_view(), name="shopping"),
    path("payment/", PaymentView.as_view(), name='payment'),
    path("unsuccess/", UnsuccessflyPaymentView.as_view(), name='unsuccess-payment'),
    path("successfly/", SuccessfltView.as_view(), name='successfly_payment'),
    path("shopping-cart/", ShoppingCartView.as_view(), name='shopping-cart'),
    path("cart-empy/", CartEmptyView.as_view(), name="cart-empy")
]
