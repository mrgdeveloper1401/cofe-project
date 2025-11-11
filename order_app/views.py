from django.shortcuts import render
from django.views.generic import TemplateView


class ShoppingView(TemplateView):
    template_name = "partials/cart/shopping.html"


class PaymentView(TemplateView):
    template_name = "partials/payment/payment.html"


class UnsuccessflyPaymentView(TemplateView):
    template_name = "partials/payment/unsuccess-payment.html"


class SuccessfltView(TemplateView):
    template_name = "partials/payment/successfly.html"


class ShoppingCartView(TemplateView):
    template_name = "partials/cart/shopping-cart.html"


class CartEmptyView(TemplateView):
    template_name = "partials/cart/cart-empty.html"
