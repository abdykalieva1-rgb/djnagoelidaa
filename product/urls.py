from django.urls import path
from .views import product, next_to_page, car_dateil, add_to_favorites, favorites_page

urlpatterns = [
    path('', product, name='product'),
    path('next_to_page/', next_to_page, name='next_to_page'),
    path('car_dateil/<int:id>/', car_dateil, name='car_dateil'),

    path('favorites/', favorites_page, name='favorites'),   # страница избранных
    path('favorites/add/<int:car_id>/', add_to_favorites, name='add_to_favorites')
]
