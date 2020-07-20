from django.contrib import admin
from django.urls import path
from core.views import consultarPlaca

urlpatterns = [
    path('admin/', admin.site.urls),
    path('placa/<str:placa>', consultarPlaca),
]
