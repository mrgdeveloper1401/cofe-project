from django.urls import path

from .views import DetailProductView


app_name = "product_app"

urlpatterns = [
    path("p/<int:id>/", DetailProductView.as_view(), name='detail-product-view')
]
