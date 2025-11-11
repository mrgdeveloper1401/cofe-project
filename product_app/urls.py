from django.urls import path

from .views import DetailProductView, ListProductView, RecentVisitProfileView


app_name = "product_app"

urlpatterns = [
    path("p/<int:id>/", DetailProductView.as_view(), name='detail-product-view'),
    path("search-product/", ListProductView.as_view(), name='list-product'),
    path("recent-visit-product/", RecentVisitProfileView.as_view(), name='recent-visit-product')
]
