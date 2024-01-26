from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from drf import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', obtain_auth_token, name='obtain_token'),
    path('api/user/', include('user.urls')),
    path('api/restaurant/', include('restaurant.urls')),
    path('api/order/', include('order.urls')),
    path('api/payment/', include('payment.urls')),
]
