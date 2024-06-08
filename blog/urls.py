from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('food_shop/<int:food_id>/', views.food_shop, name='food_shop'),
    path('food_list/', views.food_list, name='food_list'),
    path('car_list/', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car, name='car'),
    path('about/', views.about, name='about'),
]
