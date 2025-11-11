from django.urls import path
from .views import (
    HeaderView, 
    FooterView, 
    HomeView, 
    PrivacyView,
    QuestionView,
    NotFoundView
)

app_name = "core_app"


urlpatterns = [
    path("header/", HeaderView.as_view(), name='header'),
    path("footer/", FooterView.as_view(), name="footer"),
    path("main/", HomeView.as_view(), name='home'),
    path("privacy/", PrivacyView.as_view(), name='privacy'),
    path("questions/", QuestionView.as_view(), name='question'),
    path("not-found/", NotFoundView.as_view(), name="not-found")
]
