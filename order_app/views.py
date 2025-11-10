from django.shortcuts import render
from django.views.generic import TemplateView


class ShoppingView(TemplateView):
    template_name = "partials/cart/shopping.html"

