from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import (
    Service, Appointment, ServiceCategory, ServiceProvider,
    ServiceReview, Discount
)
from .serializers import (
    ServiceSerializer, AppointmentSerializer, ServiceCategorySerializer,
    ServiceProviderSerializer, ServiceReviewSerializer, FullDiscountSerializer
)


# ==== Category ====
class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [AllowAny]


# ==== Provider ====
class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    permission_classes = [AllowAny]


# ==== Service ====
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]


# ==== Appointment ====
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]


# ==== Review ====
class ServiceReviewViewSet(viewsets.ModelViewSet):
    queryset = ServiceReview.objects.all()
    serializer_class = ServiceReviewSerializer
    permission_classes = [AllowAny]


# ==== Discount ====
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = FullDiscountSerializer
    permission_classes = [AllowAny]
