from django.shortcuts import render
from django.views.generic import TemplateView


class DetailProductView(TemplateView):
    template_name = "partials/product/detail-product.html"


class ListProductView(TemplateView):
    template_name = "partials/product/search-product.html"


class RecentVisitProfileView(TemplateView):
    template_name = "partials/profile/recent-visit-product.html"
