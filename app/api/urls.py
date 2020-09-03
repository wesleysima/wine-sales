from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import ClientsViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientsViewSet, base_name='clients')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
