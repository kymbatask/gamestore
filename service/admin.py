from django.contrib import admin

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)           # Накопленные очки опыта
    level = models.IntegerField(default=1)        # Уровень пользователя
    bonuses = models.IntegerField(default=0)      # Количество бонусных баллов (например, для скидок)

    def __str__(self):
        return f"{self.user.username} - Level {self.level} - Bonuses: {self.bonuses}"

    def add_bonus(self, amount):
        self.bonuses += amount
        self.save()

    def add_xp(self, amount):
        self.xp += amount
        new_level = self.xp // 100 + 1
        if new_level > self.level:
            self.level = new_level
            # При повышении уровня, можно выдать бонусы автоматически
            self.add_bonus(10)  # например, 10 бонусных баллов за уровень
        self.save()
