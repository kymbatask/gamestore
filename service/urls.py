from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceCategoryViewSet, ServiceProviderViewSet,
    ServiceViewSet, AppointmentViewSet,
    ServiceReviewViewSet, DiscountViewSet
)

router = DefaultRouter()
router.register(r'categories', ServiceCategoryViewSet)
router.register(r'providers', ServiceProviderViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'reviews', ServiceReviewViewSet)
router.register(r'discounts', DiscountViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
]
