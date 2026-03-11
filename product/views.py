from django.shortcuts import render, get_object_or_404, redirect
from product.models import Car, Favorite


def product(request):
    return render(request, 'product.html')


def next_to_page(request):
    cars = Car.objects.all()
    favorite_ids = Favorite.objects.values_list('car_id', flat=True)

    context = {
        'cars': cars,
        'favorite_ids': favorite_ids,
    }
    return render(request, 'next_page.html', context)


def car_dateil(request, id):
    car = get_object_or_404(Car, id=id)

    context = {
        'car': car
    }
    return render(request, 'car_dateil.html', context)


def favorites_page(request):
    favorites = Favorite.objects.select_related('car').all()
    return render(request, 'add_to_favorites.html', {'favorites': favorites})


def add_to_favorites(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    favorite = Favorite.objects.filter(car=car).first()

    if favorite:
        favorite.delete()
    else:
        Favorite.objects.create(car=car)

    return redirect('next_to_page')