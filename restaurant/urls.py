from django.urls import path, include
from rest_framework import routers
from .views import RestaurantViewSet, MenuViewSet, MenuItemViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'menus', MenuViewSet, basename='menu')
router.register(r'items', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('', include(router.urls)),
    # path('restaurants', RestaurantViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list')
]
