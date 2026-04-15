from django.db import models

# Оставляем ТОЛЬКО ОДИН класс Car со всеми полями
class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    discriptions = models.TextField()  # ваша опечатка, оставляем как есть, чтобы не упал фронтенд
    image = models.ImageField(upload_to='cars/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Поле views теперь внутри основного класса
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return self.name


class Favorite(models.Model):
    # Используем строку 'Car', это безопаснее для связей
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car.name