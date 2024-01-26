from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppUserViewSet, GroupViewSet

router = DefaultRouter()
# router.register(r'users', AppUserViewSet, basename='appuser')
# router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', AppUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list')
]
