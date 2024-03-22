from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("loja/", include('loja.urls')),
    path("churubeba/", include('loja.urls'))
]
