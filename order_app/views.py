from django.shortcuts import render
from django.views.generic import TemplateView


class ShoppingView(TemplateView):
    template_name = "partials/cart/shopping.html"


class PaymentView(TemplateView):
    template_name = "partials/payment/payment.html"


class UnsuccessflyPaymentView(TemplateView):
    template_name = "partials/payment/unsuccess-payment.html"
