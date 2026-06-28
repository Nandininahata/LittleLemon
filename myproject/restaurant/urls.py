from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.index, name='test'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>/', views.single_menu_item, name='single-menu-item'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/<int:pk>/', views.booking, name='booking'),
    path('message/', views.msg),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]