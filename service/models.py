from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)                    # Название категории
    description = models.TextField(blank=True)                 # Описание категории

    def __str__(self):
        return self.name


class ServiceProvider(models.Model):
    name = models.CharField(max_length=255)                    # Имя сотрудника или компании
    bio = models.TextField(blank=True)                         # Биография или описание
    phone = models.CharField(max_length=20, blank=True)        # Телефон
    email = models.EmailField(blank=True)                      # Электронная почта

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)                    # Название услуги
    description = models.TextField(blank=True)                 # Описание услуги
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена услуги
    available = models.BooleanField(default=True)              # Доступность услуги
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True)  # Категория
    provider = models.ForeignKey(ServiceProvider, on_delete=models.SET_NULL, null=True, blank=True)  # Исполнитель

    def __str__(self):
        return self.name


class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Услуга
    provider = models.ForeignKey(ServiceProvider, on_delete=models.SET_NULL, null=True, blank=True)  # Исполнитель
    customer_name = models.CharField(max_length=255)                # Имя клиента
    customer_phone = models.CharField(max_length=20)                # Телефон клиента
    appointment_datetime = models.DateTimeField()                   # Дата и время записи
    status = models.CharField(max_length=50, choices=[
        ('scheduled', 'Запланировано'),
        ('completed', 'Завершено'),
        ('canceled', 'Отменено')
    ], default='scheduled')                                         # Статус

    def __str__(self):
        return f'{self.customer_name} - {self.service.name} @ {self.appointment_datetime}'


class ServiceReview(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Услуга
    customer_name = models.CharField(max_length=255)                # Имя клиента
    rating = models.PositiveSmallIntegerField()                     # Оценка (1-5)
    comment = models.TextField(blank=True)                          # Отзыв
    created_at = models.DateTimeField(auto_now_add=True)            # Дата отзыва

    def __str__(self):
        return f'{self.customer_name} - {self.rating}/5'


class Discount(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Услуга
    description = models.CharField(max_length=255)                  # Описание скидки
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)  # Скидка в процентах
    start_date = models.DateField()                                 # Начало действия
    end_date = models.DateField()                                   # Конец действия

    def __str__(self):
        return f'{self.discount_percent}% скидка на {self.service.name}'
