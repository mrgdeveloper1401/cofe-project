from django.shortcuts import render
from django.views.generic import TemplateView


class DetailProductView(TemplateView):
    template_name = "partials/product/detail-product.html"
