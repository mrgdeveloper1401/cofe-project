from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from decouple import config

SHOW_DEBUG_TOOLBAR = config("SHOW_DEBUG_TOOLBAR", cast=str, default=False)
SHOW_STATIC_FILES = config("SHOW_STATIC_FILES", cast=bool, default=False)

auth_urls = [
    path("auth/", include("account_app.urls", namespace="auth_app"))
]

core_urls = [
    path('core/', include("core_app.urls", namespace="core"))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + auth_urls + core_urls

if SHOW_DEBUG_TOOLBAR:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()

if SHOW_STATIC_FILES:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
