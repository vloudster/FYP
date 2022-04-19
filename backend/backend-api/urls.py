import email
from webbrowser import get
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Authors API",
        default_version="v1",
        description= "API endpoints for fyp backend project" 
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/",schema_view.with_ui("redoc", cache_timeout=0),name="schema_redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Vladimir Mauer Admin"
admin.site.site_title = "Backend Api admin portal"