# payment/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import PaymentViewSet

router = routers.DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
