from rest_framework import serializers
from .models import (
    ServiceCategory,
    ServiceProvider,
    Service,
    Appointment,
    ServiceReview,
    Discount
)


# === Service Category ===
class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'description']


# === Service Provider ===
class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['id', 'name', 'bio', 'phone', 'email']


# === Discount (used in Service) ===
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'description', 'discount_percent', 'start_date', 'end_date']


# === Service with nested category, provider, and optional discounts ===
class ServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCategory.objects.all(), source='category', write_only=True, required=False
    )

    provider = ServiceProviderSerializer(read_only=True)
    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceProvider.objects.all(), source='provider', write_only=True, required=False
    )

    current_discounts = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'description', 'price', 'available',
            'category', 'category_id',
            'provider', 'provider_id',
            'current_discounts'
        ]

    def get_current_discounts(self, obj):
        today = serializers.DateField().to_representation(serializers.datetime.date.today())
        discounts = obj.discount_set.filter(start_date__lte=today, end_date__gte=today)
        return DiscountSerializer(discounts, many=True).data


# === Appointment Serializer ===
class AppointmentSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), source='service', write_only=True
    )

    provider = ServiceProviderSerializer(read_only=True)
    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceProvider.objects.all(), source='provider', write_only=True, required=False
    )

    class Meta:
        model = Appointment
        fields = [
            'id', 'service', 'service_id',
            'provider', 'provider_id',
            'customer_name', 'customer_phone',
            'appointment_datetime', 'status'
        ]


# === Service Review Serializer ===
class ServiceReviewSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), source='service', write_only=True
    )

    class Meta:
        model = ServiceReview
        fields = [
            'id', 'service', 'service_id',
            'customer_name', 'rating', 'comment', 'created_at'
        ]


# === Discount Serializer (Full) ===
class FullDiscountSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), source='service', write_only=True
    )

    class Meta:
        model = Discount
        fields = [
            'id', 'service', 'service_id',
            'description', 'discount_percent',
            'start_date', 'end_date'
        ]
