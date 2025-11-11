from django.shortcuts import render
from django.views.generic import TemplateView


class HeaderView(TemplateView):
    template_name = "partials/header/header.html"


class FooterView(TemplateView):
    template_name = "partials/footer/footer.html"


class HomeView(TemplateView):
    template_name = "partials/main/main.html"


class PrivacyView(TemplateView):
    template_name = "partials/core/privacy.html"


class QuestionView(TemplateView):
    template_name = "partials/core/questions.html"