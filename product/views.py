from django.shortcuts import render, get_object_or_404, redirect
from product.models import Car, Favorite
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def product(request):
    return render(request, 'product.html')


from django.db.models import Q


def next_to_page(request):
    # Получаем значение из поля 'q' (как указано в вашем HTML)
    query = request.GET.get('q')

    cars = Car.objects.all()

    if query:
        # Фильтруем по названию или цвету
        cars = cars.filter(
            Q(name__icontains=query) |
            Q(color__icontains=query)
        )

    # Используем values_list, чтобы эффективно проверить наличие в избранном
    favorite_ids = Favorite.objects.values_list('car_id', flat=True)

    context = {
        'cars': cars,
        'favorite_ids': list(favorite_ids),
        'query': query,  # Передаем обратно, чтобы текст не исчезал из инпута
    }
    return render(request, 'next_page.html', context)

def car_dateil(request, id):
    car = get_object_or_404(Car, id=id)
    car.views += 1
    car.save(update_fields=['views'])

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


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('next_to_page')

    return render(request, 'register.html')
