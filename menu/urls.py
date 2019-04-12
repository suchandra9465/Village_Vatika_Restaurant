from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.MenuListView.as_view(),name='menu_list'),
    path('add/',views.add_menu_item,name='add_menu'),
]
