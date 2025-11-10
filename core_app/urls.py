from django.urls import path
from .views import HeaderView, FooterView

app_name = "core_app"


urlpatterns = [
    path("header/", HeaderView.as_view(), name='header'),
    path("footer/", FooterView.as_view(), name="footer")
]
