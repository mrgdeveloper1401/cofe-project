from django.shortcuts import render
from django.views.generic import TemplateView


class HeaderView(TemplateView):
    template_name = "partials/header/header.html"


class FooterView(TemplateView):
    template_name = "partials/footer/footer.html"
