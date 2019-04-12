from django.urls import path
from . import views

urlpatterns = [
    # path('book/',views.CreateTable.as_view(),name='book_table'),
    path('reserve_table/',views.reserve_table, name='book_table'),
    path('userlist/',views.TableListView.as_view(),name='table_user_list'),
    path('book_lawn/',views.reserve_lawn,name='book_lawn'),
    path('adminlist/',views.AdminTableList,name='admintablelist'),
]
